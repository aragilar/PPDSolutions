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
