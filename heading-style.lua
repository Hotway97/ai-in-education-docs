local text = require('text')

local CHAPTER_HEADING_LEVEL = 1
local DOCX_FORMAT = 'docx'
local PAGE_BREAK_OPENXML = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

local function isDocx()
  return FORMAT == DOCX_FORMAT
end

local function isChapterHeading(block)
  return block.t == 'Header' and block.level == CHAPTER_HEADING_LEVEL
end

local function uppercaseHeading(heading)
  return pandoc.walk_block(heading, {
    Str = function(textElement)
      return pandoc.Str(text.upper(textElement.text))
    end
  })
end

local function pageBreak()
  return pandoc.RawBlock('openxml', PAGE_BREAK_OPENXML)
end

function Header(heading)
  if isDocx() and isChapterHeading(heading) then
    return uppercaseHeading(heading)
  end
end

function Blocks(blocks)
  local transformedBlocks = {}

  for _, block in ipairs(blocks) do
    if isDocx() and isChapterHeading(block) then
      table.insert(transformedBlocks, pageBreak())
    end

    table.insert(transformedBlocks, block)
  end

  return transformedBlocks
end
