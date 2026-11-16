import Physlib.Electromagnetism.ThreeDimension.MaxwellEquations
import Lean

-- A local audit harness; no modification to Physlib source.
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option pp.universes true

#check @Electromagnetism.ThreeDimension.gaussLawElectric
#check @Electromagnetism.ThreeDimension.gaussLawMagnetic
#check @Electromagnetism.ThreeDimension.ampereLaw
#check @Electromagnetism.ThreeDimension.faradayLaw
#print axioms Electromagnetism.ThreeDimension.gaussLawElectric
#print axioms Electromagnetism.ThreeDimension.gaussLawMagnetic
#print axioms Electromagnetism.ThreeDimension.ampereLaw
#print axioms Electromagnetism.ThreeDimension.faradayLaw

-- CONTROL_INSERTION_POINT

open Lean in
run_cmd do
  let env ← getEnv
  let roots : Array Name := #[
    `Electromagnetism.ThreeDimension.gaussLawElectric,
    `Electromagnetism.ThreeDimension.gaussLawMagnetic,
    `Electromagnetism.ThreeDimension.ampereLaw,
    `Electromagnetism.ThreeDimension.faradayLaw]
  let allowed : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]
  for name in roots do
    let some info := env.checked.get.find? name | throwError "Missing root {name}"
    unless info matches .thmInfo _ do throwError "Root is not a theorem: {name}"
    let axs ← collectAxioms name
    logInfo m!"ROOT_AXIOMS {name}: {axs}"
    for ax in axs do
      unless allowed.contains ax do
        throwError "Unapproved axiom {ax} used by {name}"
    let direct := info.getUsedConstantsAsSet.toArray
    logInfo m!"DIRECT_REFERENCES {name}: {direct}"
    let mut pending := #[name]
    let mut visited : NameSet := {}
    let mut localNames : Array Name := #[]
    while !pending.isEmpty do
      let current := pending.back!
      pending := pending.pop
      if visited.contains current then continue
      visited := visited.insert current
      let some ci := env.checked.get.find? current | throwError "Missing dependency {current}"
      if let some idx := env.getModuleIdxFor? current then
        let modName := env.header.moduleNames[idx.toNat]!
        if (`Physlib).isPrefixOf modName then
          localNames := localNames.push current
          logInfo m!"PHYSLIB_DEP {name}: {current} MODULE {modName}"
      pending := pending ++ ci.getUsedConstantsAsSet.toArray
    logInfo m!"CLOSURE_COUNTS {name}: total={visited.toArray.size}, physlib={localNames.size}"
  -- The same strict scanner is exercised against quarantined controls.
  let mut controls : Nat := 0
  for (name, info) in env.checked.get.constants.toList do
    if (`AuditProbe).isPrefixOf (privateToUserName name) && !info.isUnsafe then
      controls := controls + 1
      for ax in (← collectAxioms name) do
        unless allowed.contains ax do
          throwError "Unapproved axiom {ax} used by {name}"
  logInfo m!"STRICT_AXIOM_AUDIT_PASS roots={roots.size}, controls={controls}"
