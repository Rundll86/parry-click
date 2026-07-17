class_name ConfigUtil

static var json = JSON.new()

static var serverPort: int = 0

static func loadConfig():
	var file = FileAccess.open(OS.get_executable_path().get_base_dir().path_join("../../../parry-click.json"), FileAccess.ModeFlags.READ)
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
