class_name ConfigUtil

static var json = JSON.new()

static var serverPort: int = 25565
static var currentWorkDir: String = ""

static func loadConfig():
	if OS.has_feature("editor"):
		currentWorkDir = "../../.."
	else:
		currentWorkDir = OS.get_environment("WORKDIR")
	var file = FileAccess.open(currentWorkDir.path_join("parry-click.json"), FileAccess.ModeFlags.READ)
	if file is FileAccess:
		var parsed = json.parse(file.get_as_text())
		if parsed == OK:
			var data = json.data
			serverPort = data["port"]
			print("配置加载完成", data)
		else:
			print("配置解析失败")
		file.close()
	else:
		print("配置文件不存在")
static func _static_init() -> void:
	loadConfig()
