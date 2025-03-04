from disc_solver.file_format import registries
from disc_solver.solve.shock import compute_shock
from h5preserve import open as h5open

f = h5open("sonic_library/new_miller_runs/complete_csvs/run_6/stepped_runs/2024-01-24T04:10:52.557273+11:00ForkPoolWorker-1.hdf5", registries, mode='r')
#soln = f["run"].final_solution
soln = f["run"].solutions["29"]
solns = []
for i, shock_soln in enumerate(compute_shock(
    soln, min_angle=58, max_v_θ_pre=10, min_v_θ_pre=1.5,
    plot_prefix="shock_test_plots/fixed_E_r_file_1",
)):
    print("Solution", i, "shown")
    #solns.append(shock_soln)
