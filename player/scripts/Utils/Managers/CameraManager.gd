@tool
extends Camera2D
class_name CameraManager

@export var constantOffset: Vector2 = Vector2.ZERO

static var instance: CameraManager = null
  
func _ready():
	instance = self
 
static func shake(millseconds: float, intensity: float = 10, steper: Callable = func(currentValue, _initialValue, _restPercent): return currentValue):
	var startTime = WorldManager.getCurrentTime()
	instance.shakeIntensity += intensity
	instance.shaking = true
	while WorldManager.getCurrentTime() - startTime < millseconds && instance.shaking:
		instance.shakeIntensity = steper.call(instance.shakeIntensity, intensity, 1 - (WorldManager.getCurrentTime() - startTime) / millseconds)
		await WorldManager.sceneTree.physics_frame
	shakeStop()
static func shakeStop():
	instance.shaking = false
	instance.shakeIntensity = 0
