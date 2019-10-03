# colors
# standard
h_yellow = "#fac863"
white = "#dcdcdc"
black = "#0F1519"
transparent = "#00000000"
pure_white = "#ffffff"
pure_black = "#000000"

gray_level1 = "#0F1519"
gray_level2 = "#1E2428"
gray_level3 = "#3E4246"
gray_level4 = "#4E5255"
gray_level5 = "#6D7073"
gray_level6 = "#ACAEAF"
gray_level7 = "#BCBDBE"

# normal: hsv -> h, 70, 90
red = "#e54545"
yellow = "#e5e545"
green = "#45e545"
cyan = "#45e6e5"
blue = "#4545e5"
magenta = "#e545e5"
# bright: hsv -> h, 50, 100
b_red = "#ff8080"
b_yellow = "#ffff80"
b_green = "#80ff80"
b_cyan = "#80ffff"
b_blue = "#8080ff"
b_magenta = "#ff80ff"
b_black = "#808080"  # function option color ("python -m")
# other
# hsv -> h, 60, 80
d_orange = "#cc8f52"
# hsv -> h, 50, 70
symbol_cyan = "#59b3b3"
# dark matt: hsv -> h, 25, 40
dm_green = "#608060"  # "#526652"
# dark: hsv -> h, 25, 50
d_green = "#608060"
# light matt: hsv -> h, 25, 75
lm_green = "#8fbf8f"

count = 0

def unused():
    global count
    count += 1
    return f"#ff{count:02}ff"


theme = f"""{{	
    "colors": {{
        "activityBar.background": "{gray_level2}", // standard background
        "activityBar.border": "{pure_black}", // standard border
        "activityBar.dropBackground": "{gray_level3}", // drag and drop
        "activityBar.foreground": "{white}",
        "activityBar.inactiveForeground": "{gray_level7}",
        "activityBarBadge.background": "{gray_level4}",
        "activityBarBadge.foreground": "{white}",
        "badge.background": "{gray_level3}",
        "badge.foreground": "{white}",
        "breadcrumb.activeSelectionForeground": "{white}",
        "breadcrumb.background": "{gray_level1}",
        "breadcrumb.focusForeground": "{white}",
        "breadcrumb.foreground": "{gray_level7}",
        "breadcrumbPicker.background": "{gray_level1}",
        "button.background": "{h_yellow}",
        "button.foreground": "{gray_level2}",
        "button.hoverBackground": "{b_yellow}",
        "checkbox.background": "{unused()}",
        "checkbox.border": "{unused()}",
        "checkbox.foreground": "{unused()}",
        "contrastActiveBorder": "{transparent}",
        "contrastBorder": "{transparent}",
        "debugExceptionWidget.background": "{gray_level2}",
        "debugExceptionWidget.border": "{white}",
        "debugToolBar.background": "{gray_level2}",
        "debugToolBar.border": "{h_yellow}",
        "descriptionForeground": "{white}",
        "diffEditor.border": "{h_yellow}",
        "diffEditor.insertedTextBackground": "{green}20",
        "diffEditor.insertedTextBorder": "{green}50",
        "diffEditor.removedTextBackground": "{red}20",
        "diffEditor.removedTextBorder": "{red}50",
        "dropdown.background": "{gray_level1}",
        "dropdown.border": "{gray_level1}",
        "dropdown.foreground": "{white}",
        "dropdown.listBackground": "{gray_level1}",
        "editor.background": "{gray_level1}",
        "editor.findMatchBackground": "{blue}90",
        "editor.findMatchBorder": "{transparent}",
        "editor.findMatchHighlightBackground": "{blue}50",
        "editor.findMatchHighlightBorder": "{transparent}",
        "editor.findRangeHighlightBackground": "{blue}50",
        "editor.findRangeHighlightBorder": "{transparent}",
        "editor.focusedStackFrameHighlightBackground": "{red}20",
        "editor.foreground": "{white}",
        "editor.hoverHighlightBackground": "{gray_level4}50",
        "editor.inactiveSelectionBackground": "{gray_level2}",
        "editor.lineHighlightBackground": "{gray_level4}50",
        "editor.lineHighlightBorder": "{transparent}", // border around current line not needed > transparent
        "editor.rangeHighlightBackground": "{gray_level4}15", // slight highlight for current line
        "editor.rangeHighlightBorder": "{h_yellow}", // border around current search result
        "editor.selectionBackground": "{gray_level4}40",
        "editor.selectionForeground": "{white}",
        "editor.selectionHighlightBackground": "{gray_level4}40",
        "editor.selectionHighlightBorder": "{transparent}",
        "editor.snippetFinalTabstopHighlightBackground": "{transparent}",
        "editor.snippetFinalTabstopHighlightBorder": "{transparent}",
        "editor.snippetTabstopHighlightBackground": "{transparent}",
        "editor.snippetTabstopHighlightBorder": "{b_green}",
        "editor.stackFrameHighlightBackground": "{red}20",
        "editor.wordHighlightBackground": "{h_yellow}30",
        "editor.wordHighlightBorder": "{h_yellow}",
        "editor.wordHighlightStrongBackground": "{transparent}",
        "editor.wordHighlightStrongBorder": "{transparent}",
        "editorBracketMatch.background": "{h_yellow}50",
        "editorBracketMatch.border": "{transparent}",
        "editorCodeLens.foreground": "{white}",
        "editorCursor.background": "{unused()}",
        "editorCursor.foreground": "{h_yellow}",
        "editorError.border": "{transparent}",
        "editorError.foreground": "{red}",
        "editorGroup.border": "{pure_black}",
        "editorGroup.dropBackground": "{gray_level3}",
        "editorGroup.emptyBackground": "{gray_level1}",
        "editorGroup.focusedEmptyBorder": "{h_yellow}",
        "editorGroupHeader.noTabsBackground": "{gray_level2}",
        "editorGroupHeader.tabsBackground": "{gray_level2}",
        "editorGroupHeader.tabsBorder": "{gray_level3}",
        "editorGutter.addedBackground": "{b_green}",
        "editorGutter.background": "{gray_level2}",
        "editorGutter.commentRangeForeground": "{b_blue}",
        "editorGutter.deletedBackground": "{red}",
        "editorGutter.modifiedBackground": "{gray_level3}",
        "editorHint.border": "{b_blue}",
        "editorHint.foreground": "{b_blue}",
        "editorHoverWidget.background": "{gray_level2}",
        "editorHoverWidget.border": "{gray_level3}",
        "editorHoverWidget.statusBarBackground": "{gray_level2}",
        "editorIndentGuide.activeBackground": "{gray_level5}",
        "editorIndentGuide.background": "{gray_level3}",
        "editorInfo.border": "{transparent}",
        "editorInfo.foreground": "{b_blue}", // zigzag lines for info
        "editorLineNumber.activeForeground": "{white}",
        "editorLineNumber.foreground": "{gray_level4}",
        "editorLink.activeForeground": "{gray_level3}",
        "editorMarkerNavigation.background": "{gray_level2}",
        "editorMarkerNavigationError.background": "{b_red}",
        "editorMarkerNavigationInfo.background": "{b_blue}",
        "editorMarkerNavigationWarning.background": "{b_yellow}",
        "editorOverviewRuler.addedForeground": "{h_yellow}",
        "editorOverviewRuler.border": "{transparent}",
        "editorOverviewRuler.bracketMatchForeground": "{h_yellow}",
        "editorOverviewRuler.commonContentForeground": "{h_yellow}",
        "editorOverviewRuler.currentContentForeground": "{h_yellow}",
        "editorOverviewRuler.deletedForeground": "{h_yellow}",
        "editorOverviewRuler.errorForeground": "{h_yellow}",
        "editorOverviewRuler.findMatchForeground": "{h_yellow}",
        "editorOverviewRuler.incomingContentForeground": "{h_yellow}",
        "editorOverviewRuler.infoForeground": "{h_yellow}",
        "editorOverviewRuler.modifiedForeground": "{h_yellow}",
        "editorOverviewRuler.rangeHighlightForeground": "{h_yellow}",
        "editorOverviewRuler.selectionHighlightForeground": "{h_yellow}",
        "editorOverviewRuler.warningForeground": "{h_yellow}",
        "editorOverviewRuler.wordHighlightForeground": "{h_yellow}",
        "editorOverviewRuler.wordHighlightStrongForeground": "{h_yellow}",
        "editorPane.background": "{gray_level2}",
        "editorRuler.foreground": "{green}",
        "editorSuggestWidget.background": "{gray_level2}",
        "editorSuggestWidget.border": "{gray_level1}",
        "editorSuggestWidget.foreground": "{white}",
        "editorSuggestWidget.highlightForeground": "{h_yellow}",
        "editorSuggestWidget.selectedBackground": "{gray_level3}",
        "editorUnnecessaryCode.border": "{b_blue}",
        "editorUnnecessaryCode.opacity": "{b_blue}",
        "editorWarning.border": "{transparent}",
        "editorWarning.foreground": "{h_yellow}",
        "editorWhitespace.foreground": "{gray_level4}",
        "editorWidget.background": "{gray_level1}",
        "editorWidget.border": "{gray_level3}",
        "editorWidget.foreground": "{gray_level7}",
        "editorWidget.resizeBorder": "{h_yellow}",
        "errorForeground": "{red}",
        "extensionBadge.remoteBackground": "{unused()}",
        "extensionBadge.remoteForeground": "{unused()}",
        "extensionButton.prominentBackground": "{h_yellow}",
        "extensionButton.prominentForeground": "{gray_level2}",
        "extensionButton.prominentHoverBackground": "{b_yellow}",
        "focusBorder": "{gray_level3}",
        "foreground": "{white}",
        "gitDecoration.addedResourceForeground": "{h_yellow}",
        "gitDecoration.conflictingResourceForeground": "{b_red}",
        "gitDecoration.deletedResourceForeground": "{b_red}",
        "gitDecoration.ignoredResourceForeground": "{gray_level5}",
        "gitDecoration.modifiedResourceForeground": "{h_yellow}",
        "gitDecoration.submoduleResourceForeground": "{d_orange}",
        "gitDecoration.untrackedResourceForeground": "{b_cyan}",
        "imagePreview.border": "{transparent}",
        "input.background": "{gray_level2}",
        "input.border": "{gray_level3}",
        "input.foreground": "{white}",
        "input.placeholderForeground": "{white}",
        "inputOption.activeBackground": "{gray_level1}",
        "inputOption.activeBorder": "{h_yellow}",
        "inputValidation.errorBackground": "{gray_level2}",
        "inputValidation.errorBorder": "{transparent}",
        "inputValidation.errorForeground": "{red}",
        "inputValidation.infoBackground": "{gray_level2}",
        "inputValidation.infoBorder": "{transparent}",
        "inputValidation.infoForeground": "{red}",
        "inputValidation.warningBackground": "{gray_level2}",
        "inputValidation.warningBorder": "{transparent}",
        "inputValidation.warningForeground": "{red}",
        "list.activeSelectionBackground": "{gray_level3}",
        "list.activeSelectionForeground": "{white}",
        "list.dropBackground": "{gray_level3}", // standard window background
        "list.errorForeground": "{red}", // file list error [standard red]
        "list.focusBackground": "{gray_level3}", // standard window background > no extrawurst for focus
        "list.focusForeground": "{white}",
        "list.highlightForeground": "{h_yellow}",
        "list.hoverBackground": "{gray_level2}",
        "list.hoverForeground": "{white}",
        "list.inactiveFocusBackground": "{gray_level3}",
        "list.inactiveSelectionBackground": "{gray_level3}",
        "list.inactiveSelectionForeground": "{white}",
        "list.invalidItemForeground": "{unused()}",
        "list.warningForeground": "{red}",
        "listFilterWidget.background": "{transparent}",
        "listFilterWidget.noMatchesOutline": "{red}",
        "listFilterWidget.outline": "{green}",
        "menu.background": "{gray_level2}",
        "menu.border": "{transparent}", 
        "menu.foreground": "{gray_level7}",
        "menu.selectionBackground": "{gray_level3}",
        "menu.selectionBorder": "{transparent}",
        "menu.selectionForeground": "{white}",
        "menu.separatorBackground": "{gray_level4}",
        "menubar.selectionBackground": "{gray_level3}",
        "menubar.selectionBorder": "{transparent}",
        "menubar.selectionForeground": "{white}",
        "merge.border": "{transparent}",
        "merge.commonContentBackground": "{transparent}",
        "merge.commonHeaderBackground": "{transparent}",
        "merge.currentContentBackground": "{transparent}",
        "merge.currentHeaderBackground": "{transparent}",
        "merge.incomingContentBackground": "{transparent}",
        "merge.incomingHeaderBackground": "{transparent}",
        "minimap.findMatchHighlight": "{unused()}",
        "notificationCenter.border": "{gray_level2}",
        "notificationCenterHeader.background": "{gray_level2}",
        "notificationCenterHeader.foreground": "{white}",
        "notificationLink.foreground": "{b_blue}",
        "notificationToast.border": "{gray_level2}",
        "notifications.background": "{gray_level2}",
        "notifications.border": "{transparent}",
        "notifications.foreground": "{white}",
        "panel.background": "{gray_level2}",
        "panel.border": "{pure_black}",
        "panel.dropBackground": "{gray_level1}",
        "panelInput.border": "{unused()}",
        "panelTitle.activeBorder": "{h_yellow}",
        "panelTitle.activeForeground": "{h_yellow}",
        "panelTitle.inactiveForeground": "{white}",
        "peekView.border": "{gray_level3}",
        "peekViewEditor.background": "{gray_level1}",
        "peekViewEditor.matchHighlightBackground": "{gray_level2}bb",
        "peekViewEditor.matchHighlightBorder": "{transparent}",
        "peekViewEditorGutter.background": "{gray_level2}",
        "peekViewResult.background": "{gray_level2}",
        "peekViewResult.fileForeground": "{white}",
        "peekViewResult.lineForeground": "{pure_white}",
        "peekViewResult.matchHighlightBackground": "{gray_level2}",
        "peekViewResult.selectionBackground": "{gray_level2}",
        "peekViewResult.selectionForeground": "{pure_white}",
        "peekViewTitle.background": "{gray_level2}",
        "peekViewTitleDescription.foreground": "{white}",
        "peekViewTitleLabel.foreground": "{h_yellow}",
        "pickerGroup.border": "{gray_level1}",
        "pickerGroup.foreground": "{white}",
        "progressBar.background": "{h_yellow}",
        "quickInput.background": "{gray_level2}",
        "quickInput.foreground": "{gray_level7}",
        "scrollbar.shadow": "{pure_black}cc",
        "scrollbarSlider.activeBackground": "{h_yellow}",
        "scrollbarSlider.background": "{gray_level5}",
        "scrollbarSlider.hoverBackground": "{white}",
        "selection.background": "{white}",
        "settings.checkboxBackground": "{gray_level2}",
        "settings.checkboxBorder": "{gray_level3}",
        "settings.checkboxForeground": "{white}",
        "settings.dropdownBackground": "{gray_level2}",
        "settings.dropdownBorder": "{gray_level3}",
        "settings.dropdownForeground": "{white}",
        "settings.dropdownListBorder": "{unused()}",
        "settings.headerForeground": "{h_yellow}",
        "settings.modifiedItemIndicator": "{d_orange}",
        "settings.numberInputBackground": "{gray_level2}",
        "settings.numberInputBorder": "{gray_level3}",
        "settings.numberInputForeground": "{white}",
        "settings.textInputBackground": "{gray_level2}",
        "settings.textInputBorder": "{gray_level3}",
        "settings.textInputForeground": "{white}",
        "sideBar.background": "{gray_level1}",
        "sideBar.border": "{pure_black}",
        "sideBar.dropBackground": "{white}75", // drag and drop
        "sideBar.foreground": "{white}",
        "sideBarSectionHeader.background": "{gray_level2}",
        "sideBarSectionHeader.border": "{transparent}", // Top Border on sidebar tabs, not wanted > transparent
        "sideBarSectionHeader.foreground": "{white}",
        "sideBarTitle.foreground": "{white}",
        "statusBar.background": "{gray_level2}",
        "statusBar.border": "{gray_level1}",
        "statusBar.debuggingBackground": "{gray_level2}",
        "statusBar.debuggingBorder": "{h_yellow}",
        "statusBar.debuggingForeground": "{gray_level4}",
        "statusBar.foreground": "{white}",
        "statusBar.noFolderBackground": "{gray_level2}",
        "statusBar.noFolderBorder": "{gray_level3}",
        "statusBar.noFolderForeground": "{white}",
        "statusBarItem.activeBackground": "{gray_level1}",
        "statusBarItem.hoverBackground": "{gray_level3}",
        "statusBarItem.prominentBackground": "{gray_level2}",
        "statusBarItem.prominentForeground": "{gray_level7}",
        "statusBarItem.prominentHoverBackground": "{gray_level3}",
        "statusBarItem.remoteBackground": "{gray_level2}",
        "statusBarItem.remoteForeground": "{gray_level7}",
        "tab.activeBackground": "{gray_level1}",
        "tab.activeBorder": "{h_yellow}",
        "tab.activeBorderTop": "{transparent}", // Top Border on tab, not wanted > transparent
        "tab.activeForeground": "{pure_white}",
        "tab.activeModifiedBorder": "{unused()}",
        "tab.border": "{gray_level1}", // border between tabs
        "tab.hoverBackground": "{gray_level3}",
        "tab.hoverBorder": "{white}",
        "tab.inactiveBackground": "{gray_level2}",
        "tab.inactiveForeground": "{white}",
        "tab.inactiveModifiedBorder": "{unused()}",
        "tab.unfocusedActiveBackground": "{gray_level1}",
        "tab.unfocusedActiveBorder": "{white}",
        "tab.unfocusedActiveBorderTop": "{transparent}", // Top Border on tab, not wanted > transparent
        "tab.unfocusedActiveForeground": "{pure_white}",
        "tab.unfocusedActiveModifiedBorder": "{unused()}",
        "tab.unfocusedHoverBackground": "{gray_level3}",
        "tab.unfocusedHoverBorder": "{white}",
        "tab.unfocusedInactiveForeground": "{white}",
        "tab.unfocusedInactiveModifiedBorder": "{unused()}",
        "terminal.ansiBlack": "{gray_level1}",
        "terminal.ansiBlue": "{blue}",
        "terminal.ansiBrightBlack": "{b_black}", //"#0f1c23", // function option color ("python -m")
        "terminal.ansiBrightBlue": "{b_blue}",
        "terminal.ansiBrightCyan": "{b_cyan}",
        "terminal.ansiBrightGreen": "{b_green}",
        "terminal.ansiBrightMagenta": "{b_magenta}",
        "terminal.ansiBrightRed": "{b_red}",
        "terminal.ansiBrightWhite": "{white}",
        "terminal.ansiBrightYellow": "{b_yellow}",
        "terminal.ansiCyan": "{cyan}",
        "terminal.ansiGreen": "{green}",
        "terminal.ansiMagenta": "{magenta}",
        "terminal.ansiRed": "{red}",
        "terminal.ansiWhite": "{white}",
        "terminal.ansiYellow": "{yellow}",
        "terminal.background": "{gray_level2}",
        "terminal.border": "{white}",
        "terminal.foreground": "{white}",
        "terminal.selectionBackground": "{gray_level4}40",
        "terminalCursor.background": "{black}",
        "terminalCursor.foreground": "{h_yellow}",
        "textBlockQuote.background": "{gray_level2}",
        "textBlockQuote.border": "{h_yellow}",
        "textCodeBlock.background": "{gray_level2}",
        "textLink.activeForeground": "{b_green}",
        "textLink.foreground": "{b_blue}",
        "textPreformat.foreground": "{h_yellow}",
        "textSeparator.foreground": "{h_yellow}",
        "titleBar.activeBackground": "{gray_level2}",
        "titleBar.activeForeground": "{white}",
        "titleBar.border": "{gray_level1}",
        "titleBar.inactiveBackground": "{gray_level2}",
        "titleBar.inactiveForeground": "{white}",
        "tree.indentGuidesStroke": "{gray_level4}",
        "walkThrough.embeddedEditorBackground": "{gray_level2}",
        "welcomePage.background": "{gray_level1}",
        "welcomePage.buttonBackground": "{gray_level2}",
        "welcomePage.buttonHoverBackground": "{gray_level3}",
        "widget.shadow": "{gray_level1}"
    }},
    "name": "Jungle Night",
    "tokenColors": [
        {{
            "name": "Comment",
            "scope": [
                "comment",
                "punctuation.definition.comment",
                "string.quoted.docstring.multi"
            ],
            "settings": {{
                "foreground": "{gray_level5}"
            }}
        }},
        {{
            "name": "Variable",
            "scope": [
                "variable"
            ],
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "Keyword, Storage",
            "scope": [
                "keyword",
                "storage.modifier",
                "storage.type",
                "storage.type.class.js"
            ],
            "settings": {{
                "foreground": "{dm_green}"
            }}
        }},
        {{
            "name": "Operator, Misc",
            "scope": [
                "constant.other.color",
                "keyword.operator",
                "keyword.other.substitution",
                "keyword.other.template",
                "punctuation",
                "punctuation.definition.tag",
                "punctuation.definition.tag.begin.html",
                "punctuation.definition.tag.end.html",
                "punctuation.definition.tag.html",
                "punctuation.section.embedded",
                "punctuation.separator.inheritance.php"
            ],
            "settings": {{
                "foreground": "{symbol_cyan}"
            }}
        }},
        {{
            "name": "Tag",
            "scope": [
                "entity.name.tag",
                "markup.deleted.gigutter",
                "meta.tag.sgml"
            ],
            "settings": {{
                "foreground": "{red}"
            }}
        }},
        {{
            "name": "Function, Special Method, Block Level",
            "scope": [
                "entity.name.function",
                "keyword.other.special-method",
                "meta.block-level",
                "meta.function-call",
                "support.function",
                "variable.function"
            ],
            "settings": {{
                "foreground": "#ccbb88"
            }}
        }},
        {{
            "name": "Other Variable, String Link",
            "scope": [
                "string.other.link",
                "support.other.variable"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Number, Constant, Function Argument, Tag Attribute, Embedded",
            "scope": [
                "constant.character",
                "constant.language",
                "constant.numeric",
                "keyword.other.unit",
                "support.constant",
                "variable.parameter"
            ],
            "settings": {{
                "foreground": "{d_orange}"
            }}
        }},
        {{
            "name": "String, Symbols, Inherited Class, Markup Heading",
            "scope": [
                "constant.other.key",
                "constant.other.symbol",
                "entity.other.inherited-class",
                "markup.heading",
                "markup.inserted.gigutter",
                "meta.group.braces.curly constant.other.object.key.js string.unquoted.label.js",
                "string"
            ],
            "settings": {{
                "foreground": "{lm_green}"
            }}
        }},
        {{
            "name": "Class, Support",
            "scope": [
                "entity.name.class",
                "entity.name.type.class",
                "markup.changed.gigutter",
                "meta.use.php",
                "support.class",
                "support.orther.namespace.use.php",
                "support.other.namespace.php",
                "support.type"
            ],
            "settings": {{
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "Sub-methods",
            "scope": [
                "entity.name.module.js",
                "variable.import.parameter.js",
                "variable.other.class.js"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Language methods - Variable Language",
            "scope": [
                "variable.language"
            ],
            "settings": {{
                "foreground": "{b_magenta}"
            }}
        }},
        {{
            "name": "entity.name.method.js",
            "scope": [
                "entity.name.method.js"
            ],
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "meta.method.js",
            "scope": [
                "meta.class-method.js entity.name.function.js",
                "variable.function.constructor"
            ],
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "Attributes",
            "scope": [
                "entity.other.attribute-name"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Inserted",
            "scope": [
                "markup.inserted"
            ],
            "settings": {{
                "foreground": "{b_green}"
            }}
        }},
        {{
            "name": "Deleted",
            "scope": [
                "markup.deleted"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Changed",
            "scope": [
                "markup.changed"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Regular Expressions",
            "scope": [
                "string.regexp"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "Escape Characters",
            "scope": [
                "constant.character.escape"
            ],
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "URL",
            "scope": [
                "*link*",
                "*uri*",
                "*url*"
            ],
            "settings": {{
                "fontStyle": "bold",
                "foreground": "{blue}"
            }}
        }},
        {{
            "name": "Decorators",
            "scope": [
                "tag.decorator.js entity.name.tag.js",
                "tag.decorator.js punctuation.definition.tag.js"
            ],
            "settings": {{
                "foreground": "{blue}"
            }}
        }},
        {{
            "name": "ES7 Bind Operator",
            "scope": [
                "source.js constant.other.object.key.js string.unquoted.label.js"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[CSS] - Entity",
            "scope": [
                "source.css entity",
                "source.scss entity"
            ],
            "settings": {{
                "foreground": "{b_magenta}"
            }}
        }},
        {{
            "name": "[CSS] - Entity Tag Name",
            "scope": [
                "entity.name.tag",
                "source.css entity.name",
                "source.css entity.name.tag",
                "source.css entity.name.tag entity.name.tag",
                "source.scss entity.name.tag",
                "source.scss entity.name.tag entity.name.tag"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[CSS] - Support",
            "scope": "source.css support",
            "settings": {{
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "[CSS] - Constant",
            "scope": [
                "source.css constant",
                "source.css support.constant"
            ],
            "settings": {{
                "foreground": "{yellow}"
            }}
        }},
        {{
            "name": "[CSS] - String",
            "scope": [
                "source.css punctuation.definition.string",
                "source.css string",
                "source.scss punctuation.definition.string",
                "source.scss string"
            ],
            "settings": {{
                "foreground": "{b_green}"
            }}
        }},
        {{
            "name": "[CSS] - Variable",
            "scope": "source.css variable",
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "[HTML] - Entity Name",
            "scope": "text.html.basic entity.name",
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[HTML] - Script Tag",
            "scope": "meta.tag.metadata.script.html entity.name.tag.html",
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[HTML] - Tag",
            "scope": "text.html.basic entity.name.tag",
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] Keyword",
            "scope": [
                "source.js keyword"
            ],
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] Entity",
            "scope": [
                "source.js entity",
                "source.js entity.name.tag"
            ],
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] Punctuation",
            "scope": [
                "source.js punctuation"
            ],
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] JSX Text",
            "scope": [
                "source.js meta.block"
            ],
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] - Storage Type Function",
            "scope": "source.js storage.type.function",
            "settings": {{
                "foreground": "{b_magenta}"
            }}
        }},
        {{
            "name": "[JAVASCRIPT] - Variable Language",
            "scope": "variable.language, entity.name.type.class.js",
            "settings": {{
                "foreground": "{b_red}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Changed",
            "scope": "markup.changed",
            "settings": {{
                "foreground": "{b_magenta}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Heading Punctuation",
            "scope": "punctuation.definition.heading.markdown",
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Heading Name Section",
            "scope": [
                "entity.name.section.markdown",
                "markup.heading.setext.1.markdown",
                "markup.heading.setext.2.markdown"
            ],
            "settings": {{
                "fontStyle": "bold",
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Paragraph",
            "scope": "meta.paragraph.markdown",
            "settings": {{
                "foreground": "{white}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Quote Punctuation",
            "scope": "beginning.punctuation.definition.quote.markdown",
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Quote Paragraph",
            "scope": "markup.quote.markdown meta.paragraph.markdown",
            "settings": {{
                "foreground": "{b_blue}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Separator",
            "scope": "meta.separator.markdown",
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Emphasis Bold",
            "scope": "markup.bold.markdown",
            "settings": {{
                "fontStyle": "bold",
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Emphasis Italic",
            "scope": "markup.italic.markdown",
            "settings": {{
                "foreground": "{b_blue}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Lists",
            "scope": "beginning.punctuation.definition.list.markdown",
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Link Title",
            "scope": "string.other.link.title.markdown",
            "settings": {{
                "foreground": "{b_green}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Link/Image Title",
            "scope": [
                "string.other.link.description.markdown",
                "string.other.link.description.title.markdown",
                "string.other.link.title.markdown"
            ],
            "settings": {{
                "foreground": "{b_green}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Link Address",
            "scope": [
                "markup.underline.link.image.markdown",
                "markup.underline.link.markdown"
            ],
            "settings": {{
                "foreground": "{b_blue}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Inline Code",
            "scope": [
                "fenced_code.block.language",
                "markup.inline.raw.markdown"
            ],
            "settings": {{
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "[MARKDOWN] - Code Block",
            "scope": [
                "fenced_code.block.language",
                "markup.inline.raw.markdown"
            ],
            "settings": {{
                "foreground": "{b_blue}"
            }}
        }},
        {{
            "name": "[TYPESCRIPT] - Entity Name Type",
            "scope": "source.ts entity.name.type",
            "settings": {{
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "[TYPESCRIPT] - Keyword",
            "scope": "source.ts keyword",
            "settings": {{
                "foreground": "{b_magenta}"
            }}
        }},
        {{
            "name": "[TYPESCRIPT] - Punctuation Parameters",
            "scope": "source.ts punctuation.definition.parameters",
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "name": "[TYPESCRIPT] - Punctuation Arrow Parameters",
            "scope": "meta.arrow.ts punctuation.definition.parameters",
            "settings": {{
                "foreground": "{b_cyan}"
            }}
        }},
        {{
            "scope": "token.info-token",
            "settings": {{
                "foreground": "{blue}"
            }}
        }},
        {{
            "scope": "token.warn-token",
            "settings": {{
                "foreground": "{red}"
            }}
        }},
        {{
            "scope": "token.error-token",
            "settings": {{
                "foreground": "{red}"
            }}
        }},
        {{
            "scope": "token.debug-token",
            "settings": {{
                "foreground": "{magenta}"
            }}
        }}        
    ],
	"type": "dark"
}}"""

theme_file = "themes/Jungle Night-color-theme.json"
with open(theme_file, "w") as file:
    file.write(theme)
