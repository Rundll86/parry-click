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
		match msg:
			"ping":
				responseWith("pong")

func responseWith(data: String):
	peer.set_dest_address(peer.get_packet_ip(), peer.get_packet_port())
	var state = peer.put_packet(data.to_utf8_buffer())
	if state != OK:
		print("UDP回复失败")
