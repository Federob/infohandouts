--- mermaid-config.lua
--- Filtro Lua per iniettare configurazione globale Mermaid in ogni blocco.
--- Aggiunge %%{init}%% con securityLevel 'loose' e htmlLabels per supportare
--- tag HTML (es. <br/>) nei nodi dei diagrammi.

local mermaid_init = '%%{init: {"securityLevel": "loose", "theme": "base", "flowchart": {"htmlLabels": true, "useMaxWidth": true, "curve": "basis"}}}%%'

function CodeBlock(el)
  if el.classes:includes("mermaid") then
    -- Non aggiungere se è già presente una direttiva init
    if not el.text:match("^%%%%{init:") then
      el.text = mermaid_init .. "\n" .. el.text
    end
  end
  return el
end
