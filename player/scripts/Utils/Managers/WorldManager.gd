extends Node2D
class_name WorldManager

var saveTimer: CooldownController = CooldownController.new(30000)

static var rootNode: WorldManager
static var sceneTree: SceneTree
static var runnedTime: float = 0.0

func _ready():
	rootNode = self
	sceneTree = get_tree()
	DisplayServer.window_set_mouse_passthrough([])
	DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_ALWAYS_ON_TOP, true, 0)
func _physics_process(delta):
	runnedTime += delta

static func getCurrentTime() -> float:
	return runnedTime * 1000.0
