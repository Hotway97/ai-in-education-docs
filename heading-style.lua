local text = require('text')

function Header(el)
  if el.level == 1 and FORMAT == 'docx' then
    return pandoc.walk_block(el, {
      Str = function(s)
        return pandoc.Str(text.upper(s.text))
      end
    })
  end
end

function Blocks(blocks)
  local result = {}
  for _, el in pairs(blocks) do
    if el.t == 'Header' and el.level == 1 and FORMAT == 'docx' then
      table.insert(result, pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
    end
    table.insert(result, el)
  end
  return result
end
