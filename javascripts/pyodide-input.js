// Supporto input() in Pyodide tramite window.prompt()
// Si aggancia a pyodidePromise dopo che _markdown_exec_pyodide.js l'ha creata
(function() {
    // Aspetta che pyodidePromise esista e poi inietta l'override
    function patchPyodide() {
        if (typeof pyodidePromise === 'undefined') {
            // pyodidePromise non ancora definita, riprova tra poco
            setTimeout(patchPyodide, 50);
            return;
        }

        // Wrappa la promise per iniettare l'override di input dopo l'init
        const origPromise = pyodidePromise;
        pyodidePromise = origPromise.then(async (pyodide) => {
            if (pyodide) {
                await pyodide.runPythonAsync(`
import js

def _browser_input(prompt=""):
    result = js.prompt(str(prompt))
    if result is None:
        raise EOFError("Input annullato")
    return result

__builtins__.input = _browser_input
`);
            }
            return pyodide;
        });
    }

    patchPyodide();
})();
