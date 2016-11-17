Blockly.Python['connect_to_robot'] = function(block) {
  var text_robot_ip_address = block.getFieldValue('Robot IP Adress');
  // TODO: Assemble Python into code variable.
  var code = 
	'robot = Beginner_Functions(' + text_robot_ip_address + ')\n';
  return code;
};

Blockly.Python['disconnect_from_robot'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.disconnect_from_robot()\n';
  return code;
};

Blockly.Python['reset_to_neutral'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.reset_to_neutral()\n';
  return code;
};

Blockly.Python['move_forward'] = function(block) {
  var number_time = block.getFieldValue('time');
  // TODO: Assemble Python into code variable.
  var code = 'robot.move_forward(' + number_time+ ')\n';
  return code;
};

Blockly.Python['move_backward'] = function(block) {
  var number_time = block.getFieldValue('time');
  // TODO: Assemble Python into code variable.
  var code = 'robot.move_backward(' + number_time + ')\n';
  return code;
};

Blockly.Python['say'] = function(block) {
  var text_output_string = block.getFieldValue('output string');
  // TODO: Assemble Python into code variable.
  var code = 'robot.say(' + text_output_string + ')\n';
  return code;
};

Blockly.Python['move_right'] = function(block) {
  var number_time = block.getFieldValue('time');
  // TODO: Assemble Python into code variable.
  var code = 'robot.move_right(' + number_time + ')\n';
  return code;
};

Blockly.Python['move_left'] = function(block) {
  var number_time = block.getFieldValue('time');
  // TODO: Assemble Python into code variable.
  var code = 'robot.move_left(' + number_time + ')\n';
  return code;
};

Blockly.Python['raise_right_arm'] = function(block) {
  var dropdown_right_arm_position = block.getFieldValue('right arm position');
  // TODO: Assemble Python into code variable.
  var code = 'robot.raise_right_arm(' + dropdown_right_arm_position + ')\n';
  return code;
};

Blockly.Python['raise_left_arm'] = function(block) {
  var dropdown_left_arm_position = block.getFieldValue('left arm position');
  // TODO: Assemble Python into code variable.
  var code = 'robot.raise_left_arm(' + dropdown_left_arm_position + ')\n';
  return code;
};

Blockly.Python['kick'] = function(block) {
  var dropdown_kick_leg = block.getFieldValue('kick leg');
  // TODO: Assemble Python into code variable.
  var code = 'robot.kick(' + dropdown_kick_leg + ')\n';
  return code;
};

Blockly.Python['extend_arm'] = function(block) {
  var dropdown_raise_arm = block.getFieldValue('raise arm');
  // TODO: Assemble Python into code variable.
  var code = 'robot.extend_arm(' + dropdown_raise_arm + ')\n';
  return code;
};

Blockly.Python['take_picture'] = function(block) {
  var text_filename = block.getFieldValue('filename');
  // TODO: Assemble Python into code variable.
  var code = 'robot.take_picture(' + text_filename + ')\n';
  return code;
};

Blockly.Python['play_audio'] = function(block) {
  var text_audio_filepath = block.getFieldValue('audio filepath');
  // TODO: Assemble Python into code variable.
  var code = 'robot.play_audio(' + text_audio_filepath + ')\n';
  return code;
};

Blockly.Python['sit'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.sit()\n';
  return code;
};

Blockly.Python['stand'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.stand()\n';
  return code;
};

Blockly.Python['lay_down'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.lay_down()\n';
  return code;
};