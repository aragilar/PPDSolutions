OUTPUT_DIR=plots
TARGETS=$(OUTPUT_DIR)/initial_diverge.svg

.PHONY: all clean

all: $(TARGETS)

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(OUTPUT_DIR)/initial_diverge.svg: $(OUTPUT_DIR)
	ds-diverge-plot diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 0-4 --stop 5 --filename $@

# initial convergence
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 3-10 --stop 3

# main types now visible
#ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 10-20 --stop 3 --start 1.5

# zoom in on the sonic point
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 20-30 --stop 2.1 --start 2.08

# zoom in on the sonic point no jumps
# ds-diverge-plot --show diverge/diverge-2024-07-29T13:47:38.962910+10:00.hdf5 --no-show-version --title='' --solutions 21,22,24,25,28,30 --stop 2.1 --start 2.08

# zoom in on solution
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --stop 5 --portrait --hide-roots --title '' --no-show-version --with-slow
#
# overall solution
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --stop 55 --portrait --hide-roots --title '' --no-show-version --with-alfven
#
# sonic and post sonic
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --stop 10 --portrait --hide-roots --title '' --no-show-version
#
# alfven and post alfven
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --start 10 --stop 40 --portrait --hide-roots --title '' --no-show-version --with-alfven
#
# post-alfven before mess
# ds-plot --show 2024-01-09T07:52:19.526761+00:00ForkPoolWorker-15.hdf5 final --start 40 --stop 57.5 --portrait --hide-roots --title '' --no-show-version
