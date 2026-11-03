#!/usr/bin/env node
'use strict';
// Reproduce the published Geometry Lab G3 synthetic identifiability settings.
// Run ONLY against trusted, pinned Geometry Lab source.
const fs = require('node:fs');
const crypto = require('node:crypto');
const sourcePath = process.argv[2];
if (!sourcePath) {
  console.error('Usage: node replay.cjs /path/to/Geometry/index.html [--allow-local-variant]');
  process.exit(2);
}
const expectedBlobSHA = 'b9aee1175be9a59ed4fd58c09be93a1c98529a9a';
const expectedSegmentFNV = '7e47a10c';
const bytes = fs.readFileSync(sourcePath);
const actualBlobSHA = crypto.createHash('sha1')
  .update('blob ' + bytes.length + '\0').update(bytes).digest('hex');
const html = bytes.toString('utf8');
const first = html.indexOf('function rngPRNG(');
const last = html.indexOf('const color=', first);
if (first < 0 || last < first) throw new Error('Expected function block is missing.');
const sourceFunctions = html.slice(first, last);
let h = 2166136261;
for (let i = 0; i < sourceFunctions.length; i++) {
  h ^= sourceFunctions.charCodeAt(i);
  h = Math.imul(h, 16777619);
}
const numericalFingerprint = (h >>> 0).toString(16);
if (numericalFingerprint !== expectedSegmentFNV) {
  throw new Error('Numerical functions differ from the inspected release.');
}
if (actualBlobSHA !== expectedBlobSHA && !process.argv.includes('--allow-local-variant')) {
  throw new Error('HTML file is not the pinned release. Supply exact checked-out file.');
}
const config = {
  ident: {
    mode: 'measured', seed: 1597, N: 400, kappa: -0.2,
    noise: 0.84, matterNoise: 0.15, replicates: 190
  }
};
// The extracted functions execute in a closure with ONLY the selected state.
// This is a code-execution script, not a safe parser for untrusted HTML.
const evaluate = new Function('state', sourceFunctions + '\nreturn identSim();');
const q = evaluate(config);
const nullFlags = q.nulls.filter(v => v > q.cut + 1e-15).length;
const alternativeFlags = q.alts.filter(v => v > q.cut + 1e-15).length;
const output = {
  source_git_blob_sha1: actualBlobSHA,
  expected_source_git_blob_sha1: expectedBlobSHA,
  numerical_functions_fnv32: numericalFingerprint,
  full_release_match: actualBlobSHA === expectedBlobSHA,
  config: config.ident,
  example: {
    fitted_coupling: q.medianK,
    null_SSE: q.example.sse0,
    best_fit_SSE: q.example.sse1,
    delta_SSE: q.example.delta
  },
  calibration: {
    null_trials: q.cal.length,
    percentile: 0.95,
    cutoff_delta_SSE: q.cut
  },
  holdout: {
    null_trials: q.nulls.length, null_flags: nullFlags,
    false_alarm_incidence: q.falseAlarm,
    injected_trials: q.alts.length, injected_flags: alternativeFlags,
    detection_incidence: q.power
  }
};
if (Math.abs(q.medianK + 0.2820323502393653) > 1e-10 ||
    Math.abs(q.cut - 2.3792000900125756) > 1e-10 ||
    nullFlags !== 14 || alternativeFlags !== 176) {
  throw new Error('Reproduction differs from the recorded run.');
}
console.log(JSON.stringify(output, null, 2));
