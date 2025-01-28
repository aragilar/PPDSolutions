from disc_solver.file_format import registries
from disc_solver.solve.shock import compute_shock
from h5preserve import open as h5open

f = h5open("../PPDSolutions/sonic_library/new_miller_runs/complete_csvs/run_3/stepped_runs/2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5", registries, mode='r')
soln = f["run"].final_solution
solns = []
for i, shock_soln in enumerate(compute_shock(
    soln, min_angle=58, max_v_θ_pre=10, min_v_θ_pre=1.5
)):
    print("Solution", i, "shown")
    #solns.append(shock_soln)
