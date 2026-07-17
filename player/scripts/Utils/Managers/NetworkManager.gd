extends Node
class_name NetworkManager

signal message(msg: String)

var peer: PacketPeerUDP = PacketPeerUDP.new()

func _ready() -> void:
	peer.bind(ConfigUtil.serverPort)
func _process(_delta: float) -> void:
	while peer.get_available_packet_count() > 0:
		var msg = peer.get_packet().get_string_from_utf8()
		message.emit(msg)
		print("收到消息", msg)
		var parts = msg.split(",")
		var command = parts[0]
		var args: Array = parts.slice(1)
		for i in len(args):
			var value = args[i]
			if value.is_valid_float():
				args[i] = value.to_float()
		print("已解析命令", command, args)
		match command:
			"ping":
				responseWith("pong")
			"play":
				print("正在播放")
				EffectPlayer.play("PerfectParry", Vector2(args[0], args[1]), args[2], Vector2(args[3], args[3])).shot()

func responseWith(data: String):
	peer.set_dest_address(peer.get_packet_ip(), peer.get_packet_port())
	var state = peer.put_packet(data.to_utf8_buffer())
	if state != OK:
		print("UDP回复失败")
