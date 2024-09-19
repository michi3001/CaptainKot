@0xbf5147bd62d4179d;

interface Calculator {
  add @0 (num1: Float64, num2: Float64) -> (result: Float64);
  subtract @1 (num1: Float64, num2: Float64) -> (result: Float64);
  multiply @2 (num1: Float64, num2: Float64) -> (result: Float64);
  divide @3 (num1: Float64, num2: Float64) -> (result: Float64);
}