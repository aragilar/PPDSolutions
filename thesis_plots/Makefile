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


TARGETS=$(OUT_DIR)/initial_diverge_plot.$(EXT) $(OUT_DIR)/initial_convergence_plot.$(EXT) $(OUT_DIR)/main_types_visible_plot.$(EXT) $(OUT_DIR)/zoom_in_sonic_point_diverge_plot.$(EXT) $(OUT_DIR)/zoom_in_sonic_point_diverge_no_jumps_plot.$(EXT) $(OUT_DIR)/post_alfven_before_mess_example_solution_plot.$(EXT) $(OUT_DIR)/alfven_post_alfven_example_solution_plot.$(EXT) $(OUT_DIR)/sonic_post_sonic_example_solution_plot.$(EXT) $(OUT_DIR)/slow_sonic_example_solution_plot.$(EXT) $(OUT_DIR)/overall_example_solution_plot.$(EXT)


.PHONY: all clean copy-to-thesis

all: $(TARGETS)

copy-to-thesis: $(TARGETS)
	cp $^ ../../PhDThesis/images/

clean:
	rm -f $(TARGETS)

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

$(OUT_DIR)/initial_diverge_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(HALF_PLOT_SIZE) --filename $@ --solutions 0-4 --stop 5

# initial convergence
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 3-10 --stop 3
$(OUT_DIR)/initial_convergence_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(HALF_PLOT_SIZE) --filename $@ --solutions 3-10 --stop 3

# main types now visible
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 10-20 --stop 3 --start 1.5
$(OUT_DIR)/main_types_visible_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(HALF_PLOT_SIZE) --filename $@ --solutions 10-20 --stop 3 --start 1.5

# zoom in on the sonic point
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 20-30 --stop 2.1 --start 2.08
$(OUT_DIR)/zoom_in_sonic_point_diverge_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(HALF_PLOT_SIZE) --filename $@ --solutions 20-30 --stop 2.1 --start 2.08

# zoom in on the sonic point no jumps
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 21,22,24,25,28,30 --stop 2.1 --start 2.08
$(OUT_DIR)/zoom_in_sonic_point_diverge_no_jumps_plot.$(EXT): $(OUT_DIR)
	ds-diverge-plot $(DIVERGE_PLOT_FILE) $(COMMON_PLOT_ARGS) $(HALF_PLOT_SIZE) --filename $@ --solutions 21,22,24,25,28,30 --stop 2.1 --start 2.08

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
