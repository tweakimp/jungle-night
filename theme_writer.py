# colors
# standard
h_yellow = "#ffcc66"
white = "#dcdcdc"
black = "#0F1519"
transparent = "#00000000"
unthemed = ""
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
cyan = "#45e5e5"
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
# dark matt: hsv -> h, 25, 40
dm_green = "#608060"  # "#526652"
# dark: hsv -> h, 25, 50
# d_green = "#608060"
# light matt: hsv -> h, 25, 75
lm_green = "#8fbf8f"

count = 0


def unused():
    global count
    count += 1
    return f"#ff{count:02}ff"


theme = f"""{{
    "colors": {{
        "activityBar.activeBackground": "{transparent}",
        "activityBar.activeBorder": "{pure_white}",
        "activityBar.activeFocusBorder": "{pure_white}",
        "activityBar.background": "{gray_level2}", // standard background
        "activityBar.border": "{gray_level1}", // border to the right of the whole activity bar
        "activityBar.dropBorder": "{gray_level4}", // border between icons while dragging
        "activityBar.foreground": "{pure_white}",
        "activityBar.inactiveForeground": "{gray_level7}",
        "activityBarBadge.background": "{gray_level4}",
        "activityBarBadge.foreground": "{pure_white}",
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
        "button.secondaryBackground": "{unused()}",
        "button.secondaryForeground": "{unused()}",
        "button.secondaryHoverBackground": "{unused()}",
        "checkbox.background": "{unused()}",
        "checkbox.border": "{unused()}",
        "checkbox.foreground": "{unused()}",
        "contrastActiveBorder": "{transparent}",
        "contrastBorder": "{transparent}",
        "debugConsole.errorForeground": "{red}",
        "debugConsole.infoForeground": "{green}", // stdout
        "debugConsole.sourceForeground": "{blue}",
        "debugConsole.warningForeground": "{yellow}",
        "debugConsoleInputIcon.foreground": "{gray_level6}", // little arrow that indicates an input in debug console
        "debugExceptionWidget.background": "{gray_level2}",
        "debugExceptionWidget.border": "{white}",
        "debugIcon.breakpointCurrentStackframeForeground": "{h_yellow}",
        "debugIcon.breakpointDisabledForeground": "{gray_level4}",
        "debugIcon.breakpointForeground": "{red}",
        "debugIcon.breakpointStackframeForeground": "{h_yellow}",
        "debugIcon.breakpointUnverifiedForeground": "{red}",
        // "debugIcon.continueForeground": "{unthemed}",
        // "debugIcon.disconnectForeground": "{unthemed}",
        // "debugIcon.pauseForeground": "{unthemed}",
        // "debugIcon.restartForeground": "{unthemed}",
        // "debugIcon.startForeground": "{unthemed}",
        // "debugIcon.stepIntoForeground": "{unthemed}",
        // "debugIcon.stepOutForeground": "{unthemed}",
        // "debugIcon.stepOverForeground": "{unthemed}",
        // "debugIcon.stopForeground": "{unthemed}",
        // "debugTokenExpression.boolean": "{unthemed}",
        // "debugTokenExpression.error": "{unthemed}",
        // "debugTokenExpression.name": "{unthemed}",
        // "debugTokenExpression.number": "{unthemed}",
        // "debugTokenExpression.string": "{unthemed}",
        // "debugTokenExpression.value": "{unthemed}",
        "debugToolBar.background": "{gray_level2}",
        "debugToolBar.border": "{b_green}",
        // "debugView.exceptionLabelBackground": "{unthemed}",
        // "debugView.exceptionLabelForeground": "{unthemed}",
        // "debugView.stateLabelBackground": "{unthemed}",
        // "debugView.stateLabelForeground": "{unthemed}",
        // "debugView.valueChangedHighlight": "{unthemed}",
        "descriptionForeground": "{white}",
        "diffEditor.border": "{transparent}",
        "diffEditor.diagonalFill": "{gray_level2}",
        "diffEditor.insertedTextBackground": "{green}20",
        "diffEditor.insertedTextBorder": "{green}40",
        "diffEditor.removedTextBackground": "{red}20",
        "diffEditor.removedTextBorder": "{red}40",
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
        "editor.foldBackground": "{transparent}",
        "editor.foreground": "{white}",        
        "editor.hoverHighlightBackground": "{gray_level4}50",
        "editor.inactiveSelectionBackground": "{gray_level2}",
        "editor.lineHighlightBackground": "{gray_level4}50",
        "editor.lineHighlightBorder": "{transparent}", // border around current line
        "editor.onTypeRenameBackground": "{unused()}",
        "editor.rangeHighlightBackground": "{gray_level4}15", // slight highlight for current line
        "editor.rangeHighlightBorder": "{h_yellow}", // border around current search result
        "editor.selectionBackground": "{gray_level4}50",
        "editor.selectionForeground": "{white}",
        "editor.selectionHighlightBackground": "{gray_level4}50",
        "editor.selectionHighlightBorder": "{transparent}",
        "editor.snippetFinalTabstopHighlightBackground": "{transparent}",
        "editor.snippetFinalTabstopHighlightBorder": "{transparent}",
        "editor.snippetTabstopHighlightBackground": "{transparent}",
        "editor.snippetTabstopHighlightBorder": "{b_green}",
        "editor.stackFrameHighlightBackground": "{red}20",
        "editor.symbolHighlightBackground": "{transparent}",
        "editor.symbolHighlightBorder": "{b_green}",
        "editor.wordHighlightBackground": "{h_yellow}30",
        "editor.wordHighlightBorder": "{transparent}",
        "editor.wordHighlightStrongBackground": "{transparent}",
        "editor.wordHighlightStrongBorder": "{transparent}",
        "editorBracketMatch.background": "{h_yellow}50",
        "editorBracketMatch.border": "{transparent}",
        "editorCodeLens.foreground": "{white}",
        "editorCursor.background": "{gray_level1}",
        "editorCursor.foreground": "{h_yellow}",
        "editorError.border": "{transparent}",
        "editorError.foreground": "{red}",
        "editorGroup.border": "{pure_black}",
        "editorGroup.dropBackground": "{gray_level3}",
        "editorGroup.emptyBackground": "{gray_level1}",
        "editorGroup.focusedEmptyBorder": "{h_yellow}",
        "editorGroupHeader.border": "{gray_level3}",
        "editorGroupHeader.noTabsBackground": "{gray_level2}",
        "editorGroupHeader.tabsBackground": "{gray_level2}",
        "editorGroupHeader.tabsBorder": "{gray_level3}",
        "editorGutter.addedBackground": "{b_green}",
        "editorGutter.background": "{gray_level2}",
        "editorGutter.commentRangeForeground": "{b_blue}",
        "editorGutter.deletedBackground": "{red}",
        "editorGutter.foldingControlForeground": "{pure_white}",
        "editorGutter.modifiedBackground": "{gray_level3}",
        "editorHint.border": "{b_blue}",
        "editorHint.foreground": "{b_blue}",
        "editorHoverWidget.background": "{gray_level2}",
        "editorHoverWidget.border": "{gray_level3}",
        "editorHoverWidget.foreground": "{white}",
        "editorHoverWidget.statusBarBackground": "{gray_level2}",
        "editorIndentGuide.activeBackground": "{gray_level5}",
        "editorIndentGuide.background": "{gray_level3}",
        "editorInfo.border": "{transparent}",
        "editorInfo.foreground": "{b_blue}", // zigzag lines for info
        // "editorLightBulb.foreground": "{unthemed}", // quick fix lightbulb color
        // "editorLightBulbAutoFix.foreground": "{unthemed}",
        "editorLineNumber.activeForeground": "{white}",
        "editorLineNumber.foreground": "{gray_level4}",
        "editorLink.activeForeground": "{h_yellow}",
        "editorMarkerNavigation.background": "{gray_level2}",
        "editorMarkerNavigationError.background": "{b_red}",
        "editorMarkerNavigationInfo.background": "{b_blue}",
        "editorMarkerNavigationWarning.background": "{b_yellow}",
        "editorOverviewRuler.addedForeground": "{green}",
        "editorOverviewRuler.background": "{gray_level2}",
        "editorOverviewRuler.border": "{transparent}",
        "editorOverviewRuler.bracketMatchForeground": "{h_yellow}",
        "editorOverviewRuler.commonContentForeground": "{h_yellow}",
        "editorOverviewRuler.currentContentForeground": "{h_yellow}",
        "editorOverviewRuler.deletedForeground": "{h_yellow}",
        "editorOverviewRuler.errorForeground": "{red}",
        "editorOverviewRuler.findMatchForeground": "{blue}90",
        "editorOverviewRuler.incomingContentForeground": "{h_yellow}",
        "editorOverviewRuler.infoForeground": "{transparent}",
        "editorOverviewRuler.modifiedForeground": "{h_yellow}",
        "editorOverviewRuler.rangeHighlightForeground": "{transparent}",
        "editorOverviewRuler.selectionHighlightForeground": "{transparent}",
        "editorOverviewRuler.warningForeground": "{red}",
        "editorOverviewRuler.wordHighlightForeground": "{transparent}",
        "editorOverviewRuler.wordHighlightStrongForeground": "{transparent}",
        "editorPane.background": "{gray_level2}",
        "editorRuler.foreground": "{gray_level4}",
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
        "editorWidget.background": "{gray_level2}",
        "editorWidget.border": "{gray_level3}",
        "editorWidget.foreground": "{gray_level7}",
        "editorWidget.resizeBorder": "{h_yellow}",
        "errorForeground": "{red}",
        "extensionBadge.remoteBackground": "{gray_level4}",
        "extensionBadge.remoteForeground": "{pure_white}",
        "extensionButton.prominentBackground": "{h_yellow}",
        "extensionButton.prominentForeground": "{gray_level2}",
        "extensionButton.prominentHoverBackground": "{b_yellow}",
        "focusBorder": "{transparent}", // inner border around focused widgets
        "foreground": "{white}",
        "gitDecoration.addedResourceForeground": "{h_yellow}",
        "gitDecoration.conflictingResourceForeground": "{b_red}",
        "gitDecoration.deletedResourceForeground": "{b_red}",
        "gitDecoration.ignoredResourceForeground": "{gray_level5}",
        "gitDecoration.modifiedResourceForeground": "{h_yellow}",
        "gitDecoration.submoduleResourceForeground": "{d_orange}",
        "gitDecoration.untrackedResourceForeground": "{b_cyan}",
        "icon.foreground": "{white}",
        "imagePreview.border": "{transparent}",
        "input.background": "{gray_level2}",
        "input.border": "{gray_level3}",
        "input.foreground": "{white}",
        "input.placeholderForeground": "{white}",
        "inputOption.activeForeground": "{white}",
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
        "list.deemphasizedForeground": "{gray_level5}",
        "list.dropBackground": "{gray_level3}", // standard window background
        "list.errorForeground": "{red}", // file list error [standard red]
        "list.filterMatchBackground": "{blue}90",
        "list.filterMatchBorder": "{transparent}",
        "list.focusBackground": "{gray_level3}", // standard window background > no extrawurst for focus
        "list.focusForeground": "{white}",
        "list.highlightForeground": "{h_yellow}",
        "list.hoverBackground": "{gray_level2}",
        "list.hoverForeground": "{white}",
        "list.inactiveFocusBackground": "{gray_level3}",
        "list.inactiveSelectionBackground": "{gray_level3}",
        "list.inactiveSelectionForeground": "{white}",
        "list.invalidItemForeground": "{gray_level5}",
        "list.warningForeground": "{red}",
        "listFilterWidget.background": "{gray_level1}",
        "listFilterWidget.noMatchesOutline": "{red}",
        "listFilterWidget.outline": "{green}",
        "menu.background": "{gray_level2}",
        "menu.border": "{gray_level2}",
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
        // "minimap.background": "{unthemed}",
        "minimap.errorHighlight": "{red}",
        "minimap.findMatchHighlight": "{blue}90",
        "minimap.selectionHighlight": "{gray_level4}90",
        "minimap.warningHighlight": "{red}",
        "minimapGutter.addedBackground": "{green}",
        "minimapGutter.deletedBackground": "{red}",
        "minimapGutter.modifiedBackground": "{green}",
        // "minimapSlider.activeBackground": "{unthemed}",
        // "minimapSlider.background": "{unthemed}",
        // "minimapSlider.hoverBackground": "{unthemed}",
        "notebook.cellBorderColor": "{unused()}",
        "notebook.cellHoverBackground": "{unused()}",
        "notebook.cellInsertionIndicator": "{unused()}",
        "notebook.cellStatusBarItemHoverBackground": "{unused()}",
        "notebook.cellToolbarSeparator": "{unused()}",
        "notebook.outputContainerBackgroundColor": "{unused()}",
        // "notebookStatusErrorIcon.foreground": "{unthemed}",
        // "notebookStatusRunningIcon.foreground": "{unthemed}",
        // "notebookStatusSuccessIcon.foreground": "{unthemed}",
        "notificationCenter.border": "{gray_level2}",
        "notificationCenterHeader.background": "{gray_level2}",
        "notificationCenterHeader.foreground": "{white}",
        "notificationLink.foreground": "{b_blue}",
        "notificationToast.border": "{gray_level2}",
        "notifications.background": "{gray_level2}",
        "notifications.border": "{transparent}",
        "notifications.foreground": "{white}",
        // "notificationsErrorIcon.foreground": "{unthemed}",
        // "notificationsInfoIcon.foreground": "{unthemed}",
        // "notificationsWarningIcon.foreground": "{unthemed}",
        "panel.background": "{gray_level2}",
        "panel.border": "{pure_black}",
        "panel.dropBorder": "{gray_level4}",
        "panelInput.border": "{unused()}",
        "panelSection.border": "{unused()}",
        "panelSection.dropBackground": "{unused()}",
        "panelSectionHeader.background": "{unused()}",
        "panelSectionHeader.border": "{unused()}",
        "panelSectionHeader.foreground": "{unused()}",
        "panelTitle.activeBorder": "{pure_white}",
        "panelTitle.activeForeground": "{pure_white}",
        "panelTitle.inactiveForeground": "{gray_level6}",
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
        // "problemsErrorIcon.foreground": "{unthemed}",
        // "problemsInfoIcon.foreground": "{unthemed}",
        // "problemsWarningIcon.foreground": "{unthemed}",
        "progressBar.background": "{h_yellow}",
        "quickInput.background": "{gray_level2}",
        "quickInput.foreground": "{white}",
        "quickInputTitle.background": "{gray_level2}",
        "scrollbar.shadow": "{gray_level1}",
        "scrollbarSlider.activeBackground": "{white}",
        "scrollbarSlider.background": "{gray_level5}",
        "scrollbarSlider.hoverBackground": "{white}",
        "scm.providerBorder": "{unused()}",
        "searchEditor.findMatchBackground": "{blue}90",
        "searchEditor.findMatchBorder": "{transparent}",
        "searchEditor.textInputBorder": "{gray_level3}",
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
        "statusBar.debuggingForeground": "{white}",
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
        // "symbolIcon.arrayForeground": "{unthemed}",
        // "symbolIcon.booleanForeground": "{unthemed}",
        // "symbolIcon.classForeground": "{unthemed}",
        // "symbolIcon.colorForeground": "{unthemed}",
        // "symbolIcon.constantForeground": "{unthemed}",
        // "symbolIcon.constructorForeground": "{unthemed}",
        // "symbolIcon.enumeratorForeground": "{unthemed}",
        // "symbolIcon.enumeratorMemberForeground": "{unthemed}",
        // "symbolIcon.eventForeground": "{unthemed}",
        // "symbolIcon.fieldForeground": "{unthemed}",
        // "symbolIcon.fileForeground": "{unthemed}",
        // "symbolIcon.folderForeground": "{unthemed}",
        // "symbolIcon.functionForeground": "{unthemed}",
        // "symbolIcon.interfaceForeground": "{unthemed}",
        // "symbolIcon.keyForeground": "{unthemed}",
        // "symbolIcon.keywordForeground": "{unthemed}",
        // "symbolIcon.methodForeground": "{unthemed}",
        // "symbolIcon.moduleForeground": "{unthemed}",
        // "symbolIcon.namespaceForeground": "{unthemed}",
        // "symbolIcon.nullForeground": "{unthemed}",
        // "symbolIcon.numberForeground": "{unthemed}",
        // "symbolIcon.objectForeground": "{unthemed}",
        // "symbolIcon.operatorForeground": "{unthemed}",
        // "symbolIcon.packageForeground": "{unthemed}",
        // "symbolIcon.propertyForeground": "{unthemed}",
        // "symbolIcon.referenceForeground": "{unthemed}",
        // "symbolIcon.snippetForeground": "{unthemed}",
        // "symbolIcon.stringForeground": "{unthemed}",
        // "symbolIcon.structForeground": "{unthemed}",
        // "symbolIcon.textForeground": "{unthemed}",
        // "symbolIcon.typeParameterForeground": "{unthemed}",
        // "symbolIcon.unitForeground": "{unthemed}",
        // "symbolIcon.variableForeground": "{unthemed}",
        "tab.activeBackground": "{gray_level1}",
        "tab.activeBorder": "{white}",
        "tab.activeBorderTop": "{transparent}", // Top Border on tab, not wanted > transparent
        "tab.activeForeground": "{white}",
        "tab.activeModifiedBorder": "{unused()}",
        "tab.border": "{gray_level1}", // border between tabs
        "tab.hoverBackground": "{gray_level3}",
        "tab.hoverBorder": "{transparent}",
        "tab.hoverForeground": "{pure_white}",
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
        "tab.unfocusedHoverForeground": "{pure_white}",
        "tab.unfocusedInactiveBackground": "{gray_level2}",
        "tab.unfocusedInactiveForeground": "{white}",
        "tab.unfocusedInactiveModifiedBorder": "{unused()}",
        "terminal.ansiBlack": "{gray_level1}",
        "terminal.ansiBlue": "{blue}",
        "terminal.ansiBrightBlack": "{b_black}", // function option color ("python -m")
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
        "terminal.selectionBackground": "{gray_level4}50",
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
        "widget.shadow": "{gray_level1}",
        // "window.activeBorder": "{gray_level2}",
        // "window.inactiveBorder": "{gray_level2}"
    }},
    "name": "Jungle Night",
    "tokenColors": [
        {{
            "name": "Comment",
            "scope": [
                "comment",
                "string.quoted.docstring"
            ],
            "settings": {{
                "foreground": "{gray_level5}"
            }}
        }},
        {{
            "name": "Builtins",
            "scope": [
                "support",
                "support.function.magic"
            ],
            "settings": {{
                "foreground": "{h_yellow}"
            }}
        }},
        {{
            "name": "Specials",
            "scope": [
                "variable.language.special",
                "variable.parameter.function.language.special"
            ],
            "settings": {{
                "foreground": "{b_red}"
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
                "storage"
            ],
            "settings": {{
                "foreground": "{dm_green}"
            }}
        }},
        {{
            "name": "Operator, Punctuation",
            "scope": [
                "keyword.operator",
                "punctuation.separator",
                "punctuation.definition.parameters"
            ],
            "settings": {{
                "foreground": "{gray_level6}"
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
            "name": "String, Symbols",
            "scope": [
                "constant.other.key",
                "constant.other.symbol",
                "string"
            ],
            "settings": {{
                "foreground": "{lm_green}"
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
                "foreground": "{dm_green}"
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
                "foreground": "{b_blue}"
            }}
        }},
            ],
    "type": "dark"
}}"""

theme_file = "themes/Jungle Night-color-theme.json"
with open(theme_file, "w") as file:
    file.write(theme)
print(f"Saved theme to '{theme_file}'")
