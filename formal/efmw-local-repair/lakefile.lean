import Lake
open Lake DSL

package «efmw-local-repair» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.19.0"

lean_lib EFMWLocalRepair
