
# file locations
TIRAMOLA_DIR = "/"
LOG_FILENAME = TIRAMOLA_DIR + 'logs.log'

# model names
MDP        = "MDP"
MDP_CD     = "MDP-CD"
MDP_DT     = "MDP-DT"
Q_DT       = "Q-DT"
Q_LEARNING = "Q-learning"

# model settings
MODEL                   = "model"
PARAMETERS              = "parameters"
OPTIONAL_PARAMETERS     = "optional_parameters"
INITIAL_PARAMETERS      = "initial_parameters"
MAX_OPTIONAL_PARAMETERS = "max_optional_parameters"
ACTIONS                 = "actions"
DISCOUNT                = "discount"
INITIAL_QVALUES         = "initial_qvalues"
LEARNING_RATE           = "learning_rate"
TRAINING_WINDOW         = "training_window"
REWARD_IMPORTANCE       = "reward_importance"
QUALITY_RATE            = "quality_rate"
SPLIT_ERROR             = "split_error"
MIN_MEASUREMENTS        = "min_measurements"

# supported actions
ADD_VMS    = "add_VMs"
REMOVE_VMS = "remove_VMs"
NO_OP      = "no_op"
RESIZE_VMS = "resize_VMs"

# supported parameters
NUMBER_OF_VMS    = "number_of_VMs"
RAM_SIZE         = "RAM_size"
NUMBER_OF_CPUS   = "number_of_CPUs"
STORAGE_CAPACITY = "storage_capacity"
PC_FREE_RAM      = "%_free_RAM"
PC_CPU_USAGE     = "%_CPU_usage"
IO_PER_SEC       = "I/O_per_sec"
TOTAL_LOAD       = "total_load"
PC_READ_LOAD     = "%_read_load"
TOTAL_LATENCY    = "total_latency"
WRITE_LATENCY    = "write_latency"
READ_LATENCY     = "read_latency"
PC_SERVED_LOAD   = "%_served_load"
PC_SERVED_READS  = "%_served_reads"
PC_SERVED_WRITES = "%_served_writes"

# values for parameters
VALUES = "values"
LIMITS = "limits"

# update algorithms
NO_UPDATE            = "no_update"
SINGLE_UPDATE        = "single_update"
VALUE_ITERATION      = "value_iteration"
PRIORITIZED_SWEEPING = "prioritized_sweeping"
UPDATE_ALGORITHMS    = [NO_UPDATE, SINGLE_UPDATE, VALUE_ITERATION, PRIORITIZED_SWEEPING]

# splitting algorithms for MDP-DT
MID_POINT      = "mid_point"
ANY_POINT      = "any_point"
MAX_POINT      = "max_point"
QVALUE_DIFF    = "q-value_difference"
SPLIT_CRITERIA = [MID_POINT, ANY_POINT, MAX_POINT, QVALUE_DIFF]

