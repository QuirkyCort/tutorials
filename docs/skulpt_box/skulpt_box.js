function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function stripHTML(text) {
    const regex = /</g;
    const regex2 = />/g;
    return text.replace(regex, '&lt;').replace(regex2, '&gt;');
}

function runit(event) { 
    const parent = event.target.parentElement.parentElement;
    const codeEditor = parent.querySelector('.ace_editor').env.editor;
    const canvas = parent.querySelector('.skulpt_canvas');
    const input = parent.querySelector('input');
    const output = parent.querySelector('.skulpt_output');
    if (output) {
        output.innerHTML = ''; 
    }

    let prog = codeEditor.getValue(); 

    function waitForInput() {
        return new Promise((resolve) => {
            function handler(event) {
                if (event.key == 'Enter') {
                    output.innerHTML += input.value + '\n';
                    input.removeEventListener('keydown', handler);
                    resolve(input.value);
                }
            }

            input.addEventListener('keydown', handler);
        });
    }

    Sk.inputfun = function() {
        return waitForInput();
    };
    
    let outf = function(text) {
        output.innerHTML += text;
    };

    Sk.configure({output:outf, read:builtinRead}); 
    if (canvas) {
        (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = canvas.id;
    }
    let myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(
        function(mod) {
            console.log('success');
        },
        function(err) {
            console.log(err.toString());
            output.innerHTML += '<span class="error">' + stripHTML(err.toString()) + '</span>\n';
        }
    );
} 

function initSkulptBox(ele) {
    console.log('console_only:', ele.hasAttribute('console_only'));

    const codeText = ele.textContent.trim();
    ele.textContent = '';

    const row1 = document.createElement('div');
    row1.classList.add('skulpt_row');
    ele.appendChild(row1);

    const runBtn = document.createElement('button');
    runBtn.textContent = 'Run';
    runBtn.addEventListener('click', runit);
    row1.appendChild(runBtn);

    const row2 = document.createElement('div');
    row2.classList.add('skulpt_row');
    ele.appendChild(row2);

    const leftDiv = document.createElement('div');
    leftDiv.classList.add('skulpt_left');
    row2.appendChild(leftDiv);

    const codeEditor = document.createElement('div');
    codeEditor.textContent = codeText;
    codeEditor.classList.add('ace_editor');
    leftDiv.appendChild(codeEditor);
    var editor = ace.edit(codeEditor);
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setFontSize(18);

    const rightDiv = document.createElement('div');
    rightDiv.classList.add('skulpt_right');
    row2.appendChild(rightDiv);

    if (ele.hasAttribute('console_only')) {
        const outputPre = document.createElement('pre');
        outputPre.classList.add('skulpt_output');
        outputPre.id = crypto.randomUUID();
        rightDiv.appendChild(outputPre);

        const inputField = document.createElement('input');
        inputField.type = 'text';
        rightDiv.appendChild(inputField);    
    } else {
        const canvas = document.createElement('div');
        canvas.classList.add('skulpt_canvas');
        canvas.id = crypto.randomUUID();
        rightDiv.appendChild(canvas);
    }

    if (!ele.hasAttribute('console_only') && !ele.hasAttribute('canvas_only')) {
        const row3 = document.createElement('div');
        row3.classList.add('skulpt_row');
        ele.appendChild(row3);

        const outputPre = document.createElement('pre');
        outputPre.classList.add('skulpt_output');
        outputPre.id = crypto.randomUUID();
        row3.appendChild(outputPre);

        const row4 = document.createElement('div');
        row4.classList.add('skulpt_row');
        ele.appendChild(row4);

        const inputField = document.createElement('input');
        inputField.type = 'text';
        row4.appendChild(inputField);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".skulpt_box");
    elements.forEach((e) => { initSkulptBox(e); });
});