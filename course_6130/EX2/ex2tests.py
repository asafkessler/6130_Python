import ex2a_election_code
import ex2a
import ex2b
import mytoolbox

tests_part_a = True
tests_part_b = True
maze_file = r"maze_example.csv"

if __name__ == "__main__":
    if tests_part_a:
        print("Tests part A")

        print("Tests for question A2")
        assert (ex2a.apply_threshold({"partyA": 120, "partyB": 120}, 3.25) == {"partyA": 120, "partyB": 120})
        print("Tests for question A2 - PASSED")

        print("Tests for question A3 - compute_votes_per_seat")
        assert (ex2a.compute_votes_per_seat({"partyA": 120, "partyB": 120}, 120) == 2)
        print("Tests for question A3 - compute_votes_per_seat - PASSED")

        print("Tests for question A3 - compute_seats_without_residuals")
        assert (ex2a.compute_seats_without_residuals({"partyA": 120, "partyB": 120}, 2) == {'partyA': 60, 'partyB': 60})
        print("Tests for question A3 - compute_seats_without_residuals - PASSED")

    if tests_part_b:
        print("Test part B")
        maze = mytoolbox.csv2list(maze_file, True)
        assert (ex2b.check_start_end_points(maze) == True)
        assert (ex2b.maze_solver(maze) == True)
