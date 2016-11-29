// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

fs = require('fs');
const child_process = require('child_process');
const { dialog } = require('electron').remote;
const blocks = require('../blocks/NAOBlocks');

var workspace;
// start up blockly
document.addEventListener("DOMContentLoaded", () => {
  blocks.map(block => addBlock(block));

  workspace = Blockly.inject('blocklyDiv', {
    toolbox: makeToolBox(blocks)
  });

  workspace.addChangeListener(myUpdateFunction);

  document.getElementById("save-button")
    .addEventListener("click", saveFile);
  document.getElementById("load-button")
    .addEventListener("click", loadFile);
  document.getElementById("run-button")
    .addEventListener("click", executeCode);
});

function addBlock(block) {
  Blockly.Blocks[block.type] = {
    init: function() {
      this.jsonInit(block);
    }
  };
}

function myUpdateFunction(event) {
  var code = Blockly.Python.workspaceToCode(workspace);
  document.getElementById('textarea').value = code;
}


const makeToolBox = blockList => {
  const logical_xml = `
  <category name="Control">
    <block type="controls_if"></block>
    <block type="controls_repeat_ext"></block>
    <block type="logic_compare"></block>
    <block type="math_number"></block>
    <block type="math_arithmetic"></block>
  </category>`;

  const blocks_xml = blockList.map(block => `<block type="${block.type}"></block>`).join("\n");
  return `<xml id="toolbox" style="display: none">
   ${logical_xml}
<category name="Robot">
    ${blocks_xml}
   </category>
</xml>`;
};

// Save to file
function saveFile() {
  const xml = Blockly.Xml.workspaceToDom(workspace);
  const xml_text = Blockly.Xml.domToText(xml);

  const filePath = dialog.showSaveDialog();
  fs.writeFileSync(filePath, xml_text);
  console.log('It\'s Saved');
}

function loadFile() {
  const filePaths = dialog.showOpenDialog({
    properties: ['openFile']
  });
  const xml_text = fs.readFileSync(filePaths[0]);
  workspace.clear();
  const xml = Blockly.Xml.textToDom(xml_text);
  Blockly.Xml.domToWorkspace(xml, workspace);
}

function executeCode() {
  const code = Blockly.Python.workspaceToCode(workspace);

  fs.writeFileSync("tmp.py", code);

  var extraOptions = {cwd:"../lib", shell:true};
  const spawn = require('child_process').spawn;
  const pyRunner = spawn('python', ['../electron/tmp.py'], extraOptions);

  pyRunner.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  pyRunner.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  });

  pyRunner.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}
