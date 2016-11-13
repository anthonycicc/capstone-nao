// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

fs = require('fs');
const child_process = require('child_process');
const {dialog} = require('electron').remote;

var workspace;
// start up blockly
document.addEventListener("DOMContentLoaded", () => {
  workspace = Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox')
  });

  document.getElementById("save-button").addEventListener("click", saveFile);
  document.getElementById("load-button").addEventListener("click", loadFile);
  document.getElementById("run-button").addEventListener("click", executeCode);
});


// Save to file
function saveFile(){
  const xml = Blockly.Xml.workspaceToDom(workspace);
  const xml_text = Blockly.Xml.domToText(xml);

  const filePath = dialog.showSaveDialog();
  fs.writeFileSync(filePath, xml_text);
  console.log('It\'s Saved');
}
function loadFile() {
  const filePaths = dialog.showOpenDialog({properties: ['openFile']});
  const xml_text = fs.readFileSync(filePaths[0]);
  workspace.clear();
  const xml = Blockly.Xml.textToDom(xml_text);
  Blockly.Xml.domToWorkspace(xml, workspace);
}

function executeCode() {
  const code = Blockly.Python.workspaceToCode(workspace);

  fs.writeFileSync("tmp.py", code);

  run_code = child_process.spawn('python' ['tmp.py']);
}


