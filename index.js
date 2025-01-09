async function main(entry) {
    let py = await loadPyodide()
    let mod = await (await fetch(`dw://${entry}`)).text()
    let json = JSON.parse(await (await fetch("dw://config.json")).text())
    let packages = json['packages']
    let imp = await (await fetch("dw://imports.py")).text()
    await py.loadPackage("micropip")
    const pip = py.pyimport("micropip")
    for (let i = 0; i<packages.length; i++) {
        let package = packages[i];
        await pip.install(package)
    }
    for (let i = 0; i<json['files'].length; i++) {
        let file = json['files'][i]
        let source = await (await fetch(file)).text()
        let _ = file.replace("dw://", "")
        let replaced_imp = imp.replace("$source", source).replace("$file", _)
        await py.runPythonAsync(replaced_imp)
    }
    py.runPythonAsync(mod);
    
}
