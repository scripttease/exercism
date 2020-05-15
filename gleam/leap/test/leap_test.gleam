import leap
import gleam/should

// pub fn hello_world_test() {
//   leap.hello_world()
//   |> should.equal("Hello, from leap!")
// }

pub fn year_2015_test() {
  leap.is_leap_year(2015)
  |> should.equal(False)
}

pub fn year_1996_test() {
  leap.is_leap_year(1996)
  |> should.equal(True)
}

pub fn year_2100_test() {
  leap.is_leap_year(2100)
  |> should.equal(False)
}

pub fn year_2000_test() {
  leap.is_leap_year(2000)
  |> should.equal(True)
}

pub fn year_1800_test() {
  leap.is_leap_year(1800)
  |> should.equal(False)
}