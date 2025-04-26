OUT_DIR=plots
EXT=pgf

PLOT_WIDTH=6.5 # inch = 16.5cm approx
PLOT_FULL_HEIGHT=8 # inch = 25.4 (enough space for caption hopefully)
PLOT_HALF_HEIGHT=4 # inch = 12.7 (enough space for caption hopefully)
COMMON_PLOT_ARGS=--no-show-version --title=''
FULL_PLOT_SIZE=--figsize $(PLOT_WIDTH) $(PLOT_FULL_HEIGHT)
HALF_PLOT_SIZE=--figsize $(PLOT_WIDTH) $(PLOT_HALF_HEIGHT)
DS_PLOT_COMMON_ARGS=--portrait --hide-roots

DIVERGE_PLOT_FILE=diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5
EXAMPLE_PLOT_FILE_SOLN=../sonic_library/new_miller_runs/complete_csvs/run_3/stepped_runs/2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final
FLOW_PLOT_BASIC_FILE_SOLN=../sonic_library/new_miller_runs/complete_csvs/run_6/stepped_runs/2024-01-23T11\:17\:30.323177+11\:00ForkPoolWorker-1.hdf5 11
FLOW_PLOT_BOUNCE_FILE_SOLN=../sonic_library/miller_output/miller_out_2023-02-24T08\:04\:39.105474+00\:00ForkPoolWorker-35.hdf5 final
OHM_PLOT_SOLN=../double_mod_v_r/ohm-mod_v_r-2019-01-10T16:55:25.544005+11:00.hdf5 final
AMBI_PLOT_SOLN=../ambi_ratios/good_solns/ambi-mod_v_r-2019-02-20T00:35:50.812431+11:00.hdf5 final


TARGETS=$(OUT_DIR)/initial_diverge_plot.$(EXT) $(OUT_DIR)/initial_convergence_plot.$(EXT) $(OUT_DIR)/main_types_visible_plot.$(EXT) $(OUT_DIR)/zoom_in_sonic_point_diverge_plot.$(EXT) $(OUT_DIR)/zoom_in_sonic_point_diverge_no_jumps_plot.$(EXT) $(OUT_DIR)/post_alfven_before_mess_example_solution_plot.$(EXT) $(OUT_DIR)/alfven_post_alfven_example_solution_plot.$(EXT) $(OUT_DIR)/sonic_post_sonic_example_solution_plot.$(EXT) $(OUT_DIR)/slow_sonic_example_solution_plot.$(EXT) $(OUT_DIR)/overall_example_solution_plot.$(EXT) $(OUT_DIR)/flow_plot_basic.$(EXT) $(OUT_DIR)/flow_plot_bounce.$(EXT) $(OUT_DIR)/oscillate_plot_example.$(EXT) $(OUT_DIR)/diverge_plot_example.$(EXT) $(OUT_DIR)/turn_down_plot_example.$(EXT) $(OUT_DIR)/jump_and_diverge_plot_example.$(EXT) $(OUT_DIR)/diverge_jump_down_plot_example.$(EXT) $(OUT_DIR)/ambi_full_plot.$(EXT) $(OUT_DIR)/ohm_full_plot.$(EXT) $(OUT_DIR)/flow_plot_ohm.$(EXT) $(OUT_DIR)/flow_plot_ambi.$(EXT)


.PHONY: all clean copy-to-thesis

all: $(TARGETS)

copy-to-thesis: $(TARGETS)
	cp $^ ../../PhDThesis/images/

clean:
	rm -f $(TARGETS)

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

$(OUT_DIR)/oscillate_plot_example.$(EXT): $(OUT_DIR)
	ds-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ 3 --stop 5

$(OUT_DIR)/diverge_plot_example.$(EXT): $(OUT_DIR)
	ds-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ 4 --stop 5

$(OUT_DIR)/diverge_jump_down_plot_example.$(EXT): $(OUT_DIR)
	ds-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ 10 --stop 5

$(OUT_DIR)/turn_down_plot_example.$(EXT): $(OUT_DIR)
	ds-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ 18 --stop 5

$(OUT_DIR)/jump_and_diverge_plot_example.$(EXT): $(OUT_DIR)
	ds-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ 20 --stop 5

$(OUT_DIR)/initial_diverge_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --solutions 0-4 --stop 5

# initial convergence
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 3-10 --stop 3
$(OUT_DIR)/initial_convergence_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --solutions 3-10 --stop 3

# main types now visible
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 10-20 --stop 3 --start 1.5
$(OUT_DIR)/main_types_visible_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --solutions 10-20 --stop 3 --start 1.5

# zoom in on the sonic point
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 20-30 --stop 2.1 --start 2.08
$(OUT_DIR)/zoom_in_sonic_point_diverge_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --solutions 20-30 --stop 2.1 --start 2.08

# zoom in on the sonic point no jumps
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 21,22,24,25,28,30 --stop 2.1 --start 2.08
$(OUT_DIR)/zoom_in_sonic_point_diverge_no_jumps_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --solutions 21,22,24,25,28,30 --stop 2.1 --start 2.08

# overall solution
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --portrait --hide-roots --title '' --no-show-version --with-alfven --stop 55
$(OUT_DIR)/overall_example_solution_plot.$(EXT): $(OUT_DIR)
	ds-plot $(EXAMPLE_PLOT_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --stop 55 --with-alfven
#
# slow and sonic
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --portrait --hide-roots --title '' --no-show-version --with-slow --stop 5
$(OUT_DIR)/slow_sonic_example_solution_plot.$(EXT): $(OUT_DIR)
	ds-plot $(EXAMPLE_PLOT_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --stop 5 --with-slow
#
# sonic and post sonic
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --portrait --hide-roots --title '' --no-show-version --stop 10
$(OUT_DIR)/sonic_post_sonic_example_solution_plot.$(EXT): $(OUT_DIR)
	ds-plot $(EXAMPLE_PLOT_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --stop 10
#
# alfven and post alfven
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --portrait --hide-roots --title '' --no-show-version --start 10 --stop 40 --with-alfven
$(OUT_DIR)/alfven_post_alfven_example_solution_plot.$(EXT): $(OUT_DIR)
	ds-plot $(EXAMPLE_PLOT_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --start 10 --stop 40 --with-alfven
#
# post-alfven before mess
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --portrait --hide-roots --title '' --no-show-version --start 40 --stop 57.5
$(OUT_DIR)/post_alfven_before_mess_example_solution_plot.$(EXT): $(OUT_DIR)
	ds-plot $(EXAMPLE_PLOT_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --start 40 --stop 57.5

# ds-flow-plot --show sonic_library/new_miller_runs/complete_csvs/run_6/stepped_runs/2024-01-23T11\:17\:30.323177+11\:00ForkPoolWorker-1.hdf5 11
$(OUT_DIR)/flow_plot_basic.$(EXT): $(OUT_DIR)
	ds-flow-plot $(FLOW_PLOT_BASIC_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@

# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T08\:04\:39.105474+00\:00ForkPoolWorker-35.hdf5 final --v-max 1000000
$(OUT_DIR)/flow_plot_bounce.$(EXT): $(OUT_DIR)
	ds-flow-plot $(FLOW_PLOT_BOUNCE_FILE_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --v-max 1000000

# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T07\:59\:20.194017+00\:00ForkPoolWorker-30.hdf5 final --v-step-scaling 5e-7
# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T08\:08\:24.915728+00\:00ForkPoolWorker-30.hdf5 final
# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T08\:08\:42.497008+00\:00ForkPoolWorker-23.hdf5 final
# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T08\:13\:18.040802+00\:00ForkPoolWorker-36.hdf5 final
# ds-flow-plot --show sonic_library/miller_output/miller_out_2023-02-24T08\:14\:28.342868+00\:00ForkPoolWorker-32.hdf5 final --v-max 1000000 --B-max 100000000
#
#
#

# ds-flow-plot --show double_mod_v_r/ohm-mod_v_r-2019-01-10T16:55:25.544005+11:00.hdf5 final --v-max 10000 --v-step-scaling 1e-3
$(OUT_DIR)/flow_plot_ohm.$(EXT): $(OUT_DIR)
	ds-flow-plot $(OHM_PLOT_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --v-max 10000 --v-step-scaling 1e-3

# ds-flow-plot --show ambi_ratios/good_solns/ambi-mod_v_r-2019-02-20T00:35:50.812431+11:00.hdf5 final --v-max 10000 --v-step-scaling 1e-3
$(OUT_DIR)/flow_plot_ambi.$(EXT): $(OUT_DIR)
	ds-flow-plot $(AMBI_PLOT_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) --filename $@ --v-max 10000 --v-step-scaling 1e-3

$(OUT_DIR)/ambi_full_plot.$(EXT): $(OUT_DIR)
	ds-plot $(AMBI_PLOT_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --stop 40.5 --with-alfven

$(OUT_DIR)/ohm_full_plot.$(EXT): $(OUT_DIR)
	ds-plot $(OHM_PLOT_SOLN) $(COMMON_PLOT_ARGS) $(FULL_PLOT_SIZE) $(DS_PLOT_COMMON_ARGS) --filename $@ --stop 60 --with-alfven
