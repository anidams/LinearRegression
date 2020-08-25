<!DOCTYPE html>
<!-- saved from url=(0066)http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3 -->
<html lang="en-gb"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Untitled</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./task2_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./task2_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./task2_files/MathJax.js.download" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distingish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./task2_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./task2_files/codemirror.css">


    <link rel="stylesheet" href="./task2_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./task2_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./task2_files/custom.css" type="text/css">
    <script src="./task2_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./task2_files/index.js.download" type="text/javascript"></script>
    <script src="./task2_files/index.js(1).download" type="text/javascript"></script>
    <script src="./task2_files/index.js(2).download" type="text/javascript"></script>
    <script src="./task2_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200825155117",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./task2_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./task2_files/custom.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./task2_files/extension.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */

.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */

.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-Widget {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}
.p-Widget.p-mod-hidden {
  display: none !important;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-CommandPalette {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-CommandPalette-search {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-content {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}
.p-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.p-CommandPalette-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-CommandPalette-itemIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-itemContent {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
}
.p-CommandPalette-itemShortcut {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-DockPanel {
  z-index: 0;
}
.p-DockPanel-widget {
  z-index: 0;
}
.p-DockPanel-tabBar {
  z-index: 1;
}
.p-DockPanel-handle {
  z-index: 2;
}
.p-DockPanel-handle.p-mod-hidden {
  display: none !important;
}
.p-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}
.p-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}
.p-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}
.p-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}
.p-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  -webkit-transform: translateY(-50%);
          transform: translateY(-50%);
}
.p-DockPanel-overlay {
  z-index: 3;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  pointer-events: none;
}
.p-DockPanel-overlay.p-mod-hidden {
  display: none !important;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}
.p-Menu-item {
  display: table-row;
}
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed {
  display: none !important;
}
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}
.p-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}
.p-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-MenuBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  list-style-type: none;
}
.p-MenuBar-item {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel {
  display: inline-block;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-ScrollBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-ScrollBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-ScrollBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-ScrollBar-button {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-ScrollBar-track {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: relative;
  overflow: hidden;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
}
.p-ScrollBar-thumb {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: absolute;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-SplitPanel-child {
  z-index: 0;
}
.p-SplitPanel-handle {
  z-index: 1;
}
.p-SplitPanel-handle.p-mod-hidden {
  display: none !important;
}
.p-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle {
  cursor: ew-resize;
}
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle {
  cursor: ns-resize;
}
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  -webkit-transform: translateY(-50%);
          transform: translateY(-50%);
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-TabBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-TabBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-TabBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-TabBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  list-style-type: none;
}
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-TabBar-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  overflow: hidden;
}
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-TabBar-tabLabel {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}
.p-TabBar-tab.p-mod-hidden {
  display: none !important;
}
.p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  -webkit-transition: left 150ms ease;
  transition: left 150ms ease;
}
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  -webkit-transition: top 150ms ease;
  transition: top 150ms ease;
}
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  -webkit-transition: none;
  transition: none;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-TabPanel-tabBar {
  z-index: 1;
}
.p-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\F127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    -ms-flex-item-align: start;
        align-self: flex-start;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 /* We import all of these together in a single css file because the Webpack
loader sees only one file at a time. This allows postcss to see the variable
definitions when they are used. */

 /*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

 /*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

 /**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

 /*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

 /*
 * Optional monospace font for input/output prompt.
 */

 /* Commented out in ipywidgets since we don't need it. */

 /* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

 /*
 * Added for compabitility with output area
 */

 :root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */ /* Base font size */ /* Ensures px perfect FontAwesome icons */

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */ /* Base font size */


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  /* Brand/accent */

  /* State colors (warn, error, success, info) */

  /* Cell specific styles */
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */

  /* Notebook specific styles */

  /* Console specific styles */

  /* Toolbar specific styles */
}

 /* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 /*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

 /* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

 /*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

 .jupyter-widgets.widget-tab > .p-TabBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  list-style-type: none;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  overflow: hidden;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  -webkit-transition: left 150ms ease;
  transition: left 150ms ease;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  -webkit-transition: top 150ms ease;
  transition: top 150ms ease;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  -webkit-transition: none;
  transition: none;
}

 /* End tabbar.css */

 :root { /* margin between inline elements */

    /* From Material Design Lite */
}

 .jupyter-widgets {
    margin: 2px;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    color: black;
    overflow: visible;
}

 .jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: 28px;
    height: 28px;
}

 .jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

 /* vbox and hbox */

 .widget-inline-hbox {
    /* Horizontal widgets */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
        -ms-flex-direction: row;
            flex-direction: row;
    -webkit-box-align: baseline;
        -ms-flex-align: baseline;
            align-items: baseline;
}

 .widget-inline-vbox {
    /* Vertical Widgets */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
}

 .widget-box {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    margin: 0;
    overflow: auto;
}

 .widget-gridbox {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

 .widget-hbox {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
        -ms-flex-direction: row;
            flex-direction: row;
}

 .widget-vbox {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 /* General Button Styling */

 .jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: 13px;
    cursor: pointer;

    height: 28px;
    border: 0px solid;
    line-height: 28px;
    -webkit-box-shadow: none;
            box-shadow: none;

    color: rgba(0, 0, 0, .8);
    background-color: #EEEEEE;
    border-color: #E0E0E0;
    border: none;
}

 .jupyter-button i.fa {
    margin-right: 4px;
    pointer-events: none;
}

 .jupyter-button:empty:before {
    content: "\200B"; /* zero-width space */
}

 .jupyter-widgets.jupyter-button:disabled {
    opacity: 0.6;
}

 .jupyter-button i.fa.center {
    margin-right: 0;
}

 .jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14),
                0 3px 1px -2px rgba(0, 0, 0, .2),
                0 1px 5px 0 rgba(0, 0, 0, .12);
            box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14),
                0 3px 1px -2px rgba(0, 0, 0, .2),
                0 1px 5px 0 rgba(0, 0, 0, .12);
}

 .jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    -webkit-box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14),
                0 1px 10px 0 rgba(0, 0, 0, .12),
                0 2px 4px -1px rgba(0, 0, 0, .2);
            box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14),
                0 1px 10px 0 rgba(0, 0, 0, .12),
                0 2px 4px -1px rgba(0, 0, 0, .2);
    color: rgba(0, 0, 0, .8);
    background-color: #BDBDBD;
}

 .jupyter-button:focus:enabled {
    outline: 1px solid #64B5F6;
}

 /* Button "Primary" Styling */

 .jupyter-button.mod-primary {
    color: rgba(255, 255, 255, 1.0);
    background-color: #2196F3;
}

 .jupyter-button.mod-primary.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #1976D2;
}

 .jupyter-button.mod-primary:active {
    color: rgba(255, 255, 255, 1);
    background-color: #1976D2;
}

 /* Button "Success" Styling */

 .jupyter-button.mod-success {
    color: rgba(255, 255, 255, 1.0);
    background-color: #4CAF50;
}

 .jupyter-button.mod-success.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #388E3C;
 }

 .jupyter-button.mod-success:active {
    color: rgba(255, 255, 255, 1);
    background-color: #388E3C;
 }

 /* Button "Info" Styling */

 .jupyter-button.mod-info {
    color: rgba(255, 255, 255, 1.0);
    background-color: #00BCD4;
}

 .jupyter-button.mod-info.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #0097A7;
}

 .jupyter-button.mod-info:active {
    color: rgba(255, 255, 255, 1);
    background-color: #0097A7;
}

 /* Button "Warning" Styling */

 .jupyter-button.mod-warning {
    color: rgba(255, 255, 255, 1.0);
    background-color: #FF9800;
}

 .jupyter-button.mod-warning.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #F57C00;
}

 .jupyter-button.mod-warning:active {
    color: rgba(255, 255, 255, 1);
    background-color: #F57C00;
}

 /* Button "Danger" Styling */

 .jupyter-button.mod-danger {
    color: rgba(255, 255, 255, 1.0);
    background-color: #F44336;
}

 .jupyter-button.mod-danger.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #D32F2F;
}

 .jupyter-button.mod-danger:active {
    color: rgba(255, 255, 255, 1);
    background-color: #D32F2F;
}

 /* Widget Button*/

 .widget-button, .widget-toggle-button {
    width: 148px;
}

 /* Widget Label Styling */

 /* Override Bootstrap label css */

 .jupyter-widgets label {
    margin-bottom: 0;
    margin-bottom: initial;
}

 .widget-label-basic {
    /* Basic Label */
    color: black;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 28px;
}

 .widget-label {
    /* Label */
    color: black;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 28px;
}

 .widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: black;
    text-align: right;
    margin-right: 8px;
    width: 80px;
    -ms-flex-negative: 0;
        flex-shrink: 0;
}

 .widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: black;
    text-align: center;
    line-height: 28px;
}

 /* Widget Readout Styling */

 .widget-readout {
    color: black;
    font-size: 13px;
    height: 28px;
    line-height: 28px;
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

 .widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .2),
                        0 3px 1px -2px rgba(0, 0, 0, .14),
                        0 1px 5px 0 rgba(0, 0, 0, .12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .2),
                0 3px 1px -2px rgba(0, 0, 0, .14),
                0 1px 5px 0 rgba(0, 0, 0, .12);
}

 .widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: 148px;
    min-width: 72px;
    margin-left: 4px;
}

 .widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: 4px;
    /* as wide as the widget */
    width: inherit;
}

 /* Widget Checkbox Styling */

 .widget-checkbox {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-checkbox input[type="checkbox"] {
    margin: 0px 8px 0px 0px;
    line-height: 28px;
    font-size: large;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 0;
        flex-shrink: 0;
    -ms-flex-item-align: center;
        align-self: center;
}

 /* Widget Valid Styling */

 .widget-valid {
    height: 28px;
    line-height: 28px;
    width: 148px;
    font-size: 13px;
}

 .widget-valid i:before {
    line-height: 28px;
    margin-right: 4px;
    margin-left: 4px;

    /* from the fa class in FontAwesome: https://github.com/FortAwesome/Font-Awesome/blob/49100c7c3a7b58d50baa71efef11af41a66b03d3/css/font-awesome.css#L14 */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

 .widget-valid.mod-valid i:before {
    content: "\F00C";
    color: green;
}

 .widget-valid.mod-invalid i:before {
    content: "\F00D";
    color: red;
}

 .widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

 /* Widget Text and TextArea Stying */

 .widget-textarea, .widget-text {
    width: 300px;
}

 .widget-text input[type="text"], .widget-text input[type="number"]{
    height: 28px;
    line-height: 28px;
}

 .widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-textarea textarea:disabled {
    opacity: 0.6;
}

 .widget-text input[type="text"], .widget-text input[type="number"], .widget-textarea textarea {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    padding: 4px 8px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -ms-flex-negative: 1;
        flex-shrink: 1;
    outline: none !important;
}

 .widget-textarea textarea {
    height: inherit;
    width: inherit;
}

 .widget-text input:focus, .widget-textarea textarea:focus {
    border-color: #64B5F6;
}

 /* Widget Slider */

 .widget-slider .ui-slider {
    /* Slider Track */
    border: 1px solid #BDBDBD;
    background: #BDBDBD;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

 .widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: white;
    border: 1px solid #9E9E9E;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

 /* Override jquery-ui */

 .widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: #2196F3;
    border: 1px solid #2196F3;
}

 .widget-slider .ui-slider .ui-slider-handle:active {
    background-color: #2196F3;
    border-color: #2196F3;
    z-index: 2;
    -webkit-transform: scale(1.2);
            transform: scale(1.2);
}

 .widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: #2196F3;
    z-index: 0;
}

 /* Shapes of Slider Handles */

 .widget-hslider .ui-slider .ui-slider-handle {
    width: 16px;
    height: 16px;
    margin-top: -7px;
    margin-left: -7px;
    border-radius: 50%;
    top: 0;
}

 .widget-vslider .ui-slider .ui-slider-handle {
    width: 16px;
    height: 16px;
    margin-bottom: -7px;
    margin-left: -7px;
    border-radius: 50%;
    left: 0;
}

 .widget-hslider .ui-slider .ui-slider-range {
    height: 8px;
    margin-top: -3px;
}

 .widget-vslider .ui-slider .ui-slider-range {
    width: 8px;
    margin-left: -3px;
}

 /* Horizontal Slider */

 .widget-hslider {
    width: 300px;
    height: 28px;
    line-height: 28px;

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
}

 .widgets-slider .slider-container {
    overflow: visible;
}

 .widget-hslider .slider-container {
    height: 28px;
    margin-left: 6px;
    margin-right: 6px;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
}

 .widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: 4px;
    margin-top: 12px;
    width: 100%;
}

 /* Vertical Slider */

 .widget-vbox .widget-label {
    height: 28px;
    line-height: 28px;
}

 .widget-vslider {
    /* Vertical Slider */
    height: 200px;
    width: 72px;
}

 .widget-vslider .slider-container {
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 6px;
    margin-top: 6px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 .widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: 4px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

 /* Widget Progress Styling */

 .progress-bar {
    -webkit-transition: none;
    transition: none;
}

 .progress-bar {
    height: 28px;
}

 .progress-bar {
    background-color: #2196F3;
}

 .progress-bar-success {
    background-color: #4CAF50;
}

 .progress-bar-info {
    background-color: #00BCD4;
}

 .progress-bar-warning {
    background-color: #FF9800;
}

 .progress-bar-danger {
    background-color: #F44336;
}

 .progress {
    background-color: #EEEEEE;
    border: none;
    -webkit-box-shadow: none;
            box-shadow: none;
}

 /* Horisontal Progress */

 .widget-hprogress {
    /* Progress Bar */
    height: 28px;
    line-height: 28px;
    width: 300px;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;

}

 .widget-hprogress .progress {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-top: 4px;
    margin-bottom: 4px;
    -ms-flex-item-align: stretch;
        align-self: stretch;
    /* Override bootstrap style */
    height: auto;
    height: initial;
}

 /* Vertical Progress */

 .widget-vprogress {
    height: 200px;
    width: 72px;
}

 .widget-vprogress .progress {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    width: 20px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

 /* Select Widget Styling */

 .widget-dropdown {
    height: 28px;
    width: 300px;
    line-height: 28px;
}

 .widget-dropdown > select {
    padding-right: 20px;
    border: 1px solid #9E9E9E;
    border-radius: 0;
    height: inherit;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    outline: none !important;
    -webkit-box-shadow: none;
            box-shadow: none;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    vertical-align: top;
    padding-left: 8px;
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
}

 .widget-dropdown > select:focus {
    border-color: #64B5F6;
}

 .widget-dropdown > select:disabled {
    opacity: 0.6;
}

 /* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */

 .widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

 /* Select and SelectMultiple */

 .widget-select {
    width: 300px;
    line-height: 28px;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    -webkit-box-align: start;
        -ms-flex-align: start;
            align-items: flex-start;
}

 .widget-select > select {
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

 .widget-select > select:focus {
    border-color: #64B5F6;
}

 .wiget-select > select > option {
    padding-left: 4px;
    line-height: 28px;
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(28px - var(--jp-widgets-font-size) / 2);
    padding-bottom: calc(28px - var(--jp-widgets-font-size) / 2);
}

 /* Toggle Buttons Styling */

 .widget-toggle-buttons {
    line-height: 28px;
}

 .widget-toggle-buttons .widget-toggle-button {
    margin-left: 2px;
    margin-right: 2px;
}

 .widget-toggle-buttons .jupyter-button:disabled {
    opacity: 0.6;
}

 /* Radio Buttons Styling */

 .widget-radio {
    width: 300px;
    line-height: 28px;
}

 .widget-radio-box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-bottom: 8px;
}

 .widget-radio-box label {
    height: 20px;
    line-height: 20px;
    font-size: 13px;
}

 .widget-radio-box input {
    height: 20px;
    line-height: 20px;
    margin: 0 8px 0 1px;
    float: left;
}

 /* Color Picker Styling */

 .widget-colorpicker {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-colorpicker > .widget-colorpicker-input {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    min-width: 72px;
}

 .widget-colorpicker input[type="color"] {
    width: 28px;
    height: 28px;
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    border-left: none;
    -webkit-box-flex: 0;
        -ms-flex-positive: 0;
            flex-grow: 0;
    -ms-flex-negative: 0;
        flex-shrink: 0;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    -ms-flex-item-align: stretch;
        align-self: stretch;
    outline: none !important;
}

 .widget-colorpicker.concise input[type="color"] {
    border-left: 1px solid #9E9E9E;
}

 .widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: #64B5F6;
}

 .widget-colorpicker input[type="text"] {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    outline: none !important;
    height: 28px;
    line-height: 28px;
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    font-size: 13px;
    padding: 4px 8px;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -ms-flex-negative: 1;
        flex-shrink: 1;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
}

 .widget-colorpicker input[type="text"]:disabled {
    opacity: 0.6;
}

 /* Date Picker Styling */

 .widget-datepicker {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-datepicker input[type="date"] {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: 28px;
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    padding: 4px 8px;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
}

 .widget-datepicker input[type="date"]:focus {
    border-color: #64B5F6;
}

 .widget-datepicker input[type="date"]:invalid {
    border-color: #FF9800;
}

 .widget-datepicker input[type="date"]:disabled {
    opacity: 0.6;
}

 /* Play Widget */

 .widget-play {
    width: 148px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .widget-play .jupyter-button {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    height: auto;
}

 .widget-play .jupyter-button:disabled {
    opacity: 0.6;
}

 /* Tab Widget */

 .jupyter-widgets.widget-tab {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

 .jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    -webkit-box-align: end;
        -ms-flex-align: end;
            align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

 .jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    margin: 0;
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    padding: 15px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    overflow: auto;
}

 .jupyter-widgets.widget-tab > .p-TabBar {
    font: 13px Helvetica, Arial, sans-serif;
    min-height: 25px;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    -webkit-box-flex: 0;
        -ms-flex: 0 1 144px;
            flex: 0 1 144px;
    min-width: 35px;
    min-height: 25px;
    line-height: 24px;
    margin-left: -1px;
    padding: 0px 10px;
    background: #EEEEEE;
    color: rgba(0, 0, 0, .5);
    border: 1px solid #9E9E9E;
    border-bottom: none;
    position: relative;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: rgba(0, 0, 0, 1.0);
    /* We want the background to match the tab content background */
    background: white;
    min-height: 26px;
    -webkit-transform: translateY(1px);
            transform: translateY(1px);
    overflow: visible;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: -1px;
    left: -1px;
    content: '';
    height: 2px;
    width: calc(100% + 2px);
    background: #2196F3;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: white;
    color: rgba(0, 0, 0, .8);
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\F00D'; /* close */
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: 24px;
}

 /* Accordion Widget */

 .p-Collapse {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .p-Collapse-header {
    padding: 4px;
    cursor: pointer;
    color: rgba(0, 0, 0, .5);
    background-color: #EEEEEE;
    border: 1px solid #9E9E9E;
    padding: 10px 15px;
    font-weight: bold;
}

 .p-Collapse-header:hover {
    background-color: white;
    color: rgba(0, 0, 0, .8);
}

 .p-Collapse-open > .p-Collapse-header {
    background-color: white;
    color: rgba(0, 0, 0, 1.0);
    cursor: default;
    border-bottom: none;
}

 .p-Collapse .p-Collapse-header::before {
    content: '\F0DA\A0';  /* caret-right, non-breaking space */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

 .p-Collapse-open > .p-Collapse-header::before {
    content: '\F0D7\A0'; /* caret-down, non-breaking space */
}

 .p-Collapse-contents {
    padding: 15px;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    border-left: 1px solid #9E9E9E;
    border-right: 1px solid #9E9E9E;
    border-bottom: 1px solid #9E9E9E;
    overflow: auto;
}

 .p-Accordion {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .p-Accordion .p-Collapse {
    margin-bottom: 0;
}

 .p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}

 /* HTML widget */

 .widget-html, .widget-htmlmath {
    font-size: 13px;
}

 .widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    -ms-flex-item-align: stretch;
        align-self: stretch;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: 28px;
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8888/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app command_mode" data-jupyter-api-token="949bb0fba33b53a78d16e1a1d6548abe3e1b8384f236734f" data-base-url="/" data-ws-url="" data-notebook-name="Untitled.ipynb" data-notebook-path="Untitled.ipynb" dir="ltr"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=949bb0fba33b53a78d16e1a1d6548abe3e1b8384f236734f" title="dashboard">
      <img src="./task2_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">Untitled</span>
    <span class="checkpoint_status" title="Tue, 25 Aug 2020 15:52">Last Checkpoint: 2 hours ago</span>
    <span class="autosave_status">(autosaved)</span>
</span>

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./task2_files/logo-64x64.png" title="Python 3" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="Kernel Idle"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="Command Mode"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" disabled="disabled" style="cursor: help;"><span title="Javascript enabled for notebook display">Trusted</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">File</a>
                    <ul id="file_menu" class="dropdown-menu">
                        <li id="new_notebook" class="dropdown-submenu">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">New Notebook</a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu"><li id="new-notebook-submenu-python3"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python 3</a></li></ul>
                        </li>
                        <li id="open_notebook" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="copy_notebook" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Make a Copy...</a></li>
                        <li id="save_notebook_as" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Save as...</a></li>
                        <li id="rename_notebook"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Rename...</a></li>
                        <li id="save_checkpoint"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Save and Checkpoint</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="restore_checkpoint" class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Revert to Checkpoint</a>
                          <ul class="dropdown-menu"><li><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Tuesday, 25 August 2020 15:52</a></li></ul>
                        </li>
                        <li class="divider"></li>
                        <li id="print_preview"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Print Preview</a></li>
                        <li class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Download as</a>
                            <ul id="download_menu" class="dropdown-menu">
                                <li id="download_ipynb"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Notebook (.ipynb)</a></li>
                                <li id="download_script"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python (.py)</a></li>
                                <li id="download_html"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">HTML (.html)</a></li>
                                <li id="download_slides"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Reveal.js slides (.html)</a></li>
                                <li id="download_markdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Markdown (.md)</a></li>
                                <li id="download_rst"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">reST (.rst)</a></li>
                                <li id="download_latex"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">LaTeX (.tex)</a></li>
                                <li id="download_pdf"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">PDF via LaTeX (.pdf)</a></li>
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">asciidoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_custom">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">custom (.txt)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">custom (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">latex (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">pdf (.tex)</a>
                                </li>
                                
                                <li id="download_python">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">python (.py)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">rst (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">custom (.txt)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">slides (.slides.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider"></li>
                        <li id="trust_notebook" title="Trust the output of this notebook" class="disabled">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Trusted Notebook</a></li>
                        <li class="divider"></li>
                        <li id="close_and_halt" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Close and Halt</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu">
                        <li id="cut_cell"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Cut Cells</a></li>
                        <li id="copy_cell"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Copy Cells</a></li>
                        <li id="paste_cell_above" class=""><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Paste Cells Above</a></li>
                        <li id="paste_cell_below" class=""><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Paste Cells Below</a></li>
                        <li id="paste_cell_replace" class=""><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Delete Cells</a></li>
                        <li id="undelete_cell" class=""><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Undo Delete Cells</a></li>
                        <li class="divider"></li>
                        <li id="split_cell"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Split Cell</a></li>
                        <li id="merge_cell_above"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Merge Cell Above</a></li>
                        <li id="merge_cell_below"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Merge Cell Below</a></li>
                        <li class="divider"></li>
                        <li id="move_cell_up"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Move Cell Up</a></li>
                        <li id="move_cell_down"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Move Cell Down</a></li>
                        <li class="divider"></li>
                        <li id="edit_nb_metadata"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Edit Notebook Metadata</a></li>
                        <li class="divider"></li>
                        <li id="find_and_replace"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#"> Find and Replace </a></li>
                        <li class="divider"></li>
                        <li id="cut_cell_attachments"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Paste Cell Attachments</a></li>
                        <li class="divider"></li>
                        <li id="insert_image" class="disabled"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#"> Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">View</a>
                    <ul id="view_menu" class="dropdown-menu">
                        <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Line Numbers</a>
                        </li>
                        <li id="menu-cell-toolbar" class="dropdown-submenu">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="None"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">None</a></li><li data-name="Edit%20Metadata"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Edit Metadata</a></li><li data-name="Raw%20Cell%20Format"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Raw Cell Format</a></li><li data-name="Slideshow"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Slideshow</a></li><li data-name="Attachments"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Attachments</a></li><li data-name="Tags"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu">
                        <li id="insert_cell_above" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Insert Cell Above</a></li>
                        <li id="insert_cell_below" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Insert Cell Below</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu">
                        <li id="run_cell" title="Run this cell, and move cursor to the next one">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells</a></li>
                        <li id="run_cell_select_below" title="Run this cell, select below">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells and Select Below</a></li>
                        <li id="run_cell_insert_below" title="Run this cell, insert below">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells and Insert Below</a></li>
                        <li id="run_all_cells" title="Run all cells in the notebook">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All</a></li>
                        <li id="run_all_cells_above" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All Above</a></li>
                        <li id="run_all_cells_below" title="Run this cell and all cells below it">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All Below</a></li>
                        <li class="divider"></li>
                        <li id="change_cell_type" class="dropdown-submenu" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Cell Type</a>
                            <ul class="dropdown-menu">
                              <li id="to_code" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Code</a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Markdown</a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Raw NBConvert</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li id="current_outputs" class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Current Outputs</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_current_output" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle</a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">All Output</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_all_output" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Interrupt</a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart</a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Shutdown</a>
                        </li>
                        <li class="divider"></li>
                        <li id="menu-change-kernel" class="dropdown-submenu">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python 3</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Keyboard Shortcuts</a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="Opens in a new window" href="https://docs.python.org/3.7?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://ipython.org/documentation.html?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/numpy/reference/?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/scipy/reference/?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://matplotlib.org/contents.html?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="http://docs.sympy.org/latest/index.html?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://pandas.pydata.org/pandas-docs/stable/?v=20200825155117"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="Save and Checkpoint" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="insert cell below" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="cut selected cells" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="copy selected cells" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="paste cells below" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="move selected cells up" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="move selected cells down" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" title="Run" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-step-forward fa"></i><span class="toolbar-btn-label">Run</span></button><button class="btn btn-default" title="interrupt the kernel" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="restart the kernel (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="restart the kernel, then re-run the whole notebook (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" class="form-control select-xs"><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw NBConvert</option><option value="heading">Heading</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group"><button class="btn btn-default" title="open the command palette" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 466px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell rendered selected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[49]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 90.5938px; left: 113.375px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 516.688px; margin-bottom: -17px; border-right-width: 13px; min-height: 130px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 113.375px; top: 85px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">pandas</span> <span class="cm-keyword">as</span> <span class="cm-variable">pd</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span>.<span class="cm-property">pyplot</span> <span class="cm-keyword">as</span> <span class="cm-variable">plt</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">seaborn</span> <span class="cm-keyword">as</span> <span class="cm-variable">sns</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-operator">%</span><span class="cm-variable">matplotlib</span> <span class="cm-variable">inline</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">sklearn</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">sklearn</span>.<span class="cm-property">metrics</span> <span class="cm-keyword">import</span> <span class="cm-variable">mean_squared_error</span>,<span class="cm-variable">mean_absolute_error</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 130px;"></div><div class="CodeMirror-gutters" style="display: none; height: 143px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[18]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 498.281px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 501.281px; margin-bottom: -17px; border-right-width: 13px; min-height: 45px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 498.281px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span> <span class="cm-operator">=</span> <span class="cm-variable">pd</span>.<span class="cm-property">read_csv</span>(<span class="cm-string">"http://bit.ly/w-data"</span>)<span class="cm-comment">#importing the data</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span>.<span class="cm-property">shape</span> <span class="cm-comment">#gives no of rows and columns</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 45px;"></div><div class="CodeMirror-gutters" style="display: none; height: 58px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[18]:</bdi></div><div class="output_subarea output_text output_result"><pre>(25, 2)</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[19]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 282.75px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 285.75px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 282.75px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span>.<span class="cm-property">head</span>(<span class="cm-number">25</span>)<span class="cm-comment">#displaying the data</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[19]:</bdi></div><div class="output_subarea output_html rendered_html output_result"><div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hours</th>
      <th>Scores</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.5</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.1</td>
      <td>47</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.2</td>
      <td>27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8.5</td>
      <td>75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.5</td>
      <td>20</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9.2</td>
      <td>88</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.5</td>
      <td>60</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.3</td>
      <td>81</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.7</td>
      <td>25</td>
    </tr>
    <tr>
      <th>10</th>
      <td>7.7</td>
      <td>85</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.9</td>
      <td>62</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.5</td>
      <td>41</td>
    </tr>
    <tr>
      <th>13</th>
      <td>3.3</td>
      <td>42</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.1</td>
      <td>17</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.9</td>
      <td>95</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2.5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.9</td>
      <td>24</td>
    </tr>
    <tr>
      <th>18</th>
      <td>6.1</td>
      <td>67</td>
    </tr>
    <tr>
      <th>19</th>
      <td>7.4</td>
      <td>69</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2.7</td>
      <td>30</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4.8</td>
      <td>54</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3.8</td>
      <td>35</td>
    </tr>
    <tr>
      <th>23</th>
      <td>6.9</td>
      <td>76</td>
    </tr>
    <tr>
      <th>24</th>
      <td>7.8</td>
      <td>86</td>
    </tr>
  </tbody>
</table>
</div></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[20]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 359.703px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 362.703px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 359.703px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span>.<span class="cm-property">describe</span>()<span class="cm-comment">#statistical details of data</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[20]:</bdi></div><div class="output_subarea output_html rendered_html output_result"><div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hours</th>
      <th>Scores</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>25.000000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.012000</td>
      <td>51.480000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.525094</td>
      <td>25.286887</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.100000</td>
      <td>17.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.700000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.800000</td>
      <td>47.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.400000</td>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.200000</td>
      <td>95.000000</td>
    </tr>
  </tbody>
</table>
</div></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[21]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 498.328px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="false"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 516.734px; margin-bottom: -17px; border-right-width: 13px; min-height: 96px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 498.328px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span><span class="cm-operator">=</span><span class="cm-string">'Hours'</span>, <span class="cm-variable">y</span><span class="cm-operator">=</span><span class="cm-string">'Scores'</span>, <span class="cm-variable">style</span><span class="cm-operator">=</span><span class="cm-string">'o'</span>)<span class="cm-comment">#plotting a graphx  </span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">title</span>(<span class="cm-string">'No of hours studied vs. Scores'</span>)  </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">xlabel</span>(<span class="cm-string">'Hours'</span>)  </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">ylabel</span>(<span class="cm-string">'Scores'</span>)  </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">show</span>()</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 96px;"></div><div class="CodeMirror-gutters" style="display: none; height: 109px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[22]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 22.5938px; left: 205.781px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 224.188px; margin-bottom: -17px; border-right-width: 13px; min-height: 45px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 205.781px; top: 17px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">x</span><span class="cm-operator">=</span><span class="cm-variable">dataset</span>.<span class="cm-property">iloc</span>[:,:<span class="cm-operator">-</span><span class="cm-number">1</span>].<span class="cm-property">values</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y</span><span class="cm-operator">=</span><span class="cm-variable">dataset</span>.<span class="cm-property">iloc</span>[:,<span class="cm-number">1</span>].<span class="cm-property">values</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 45px;"></div><div class="CodeMirror-gutters" style="display: none; height: 58px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[27]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 405.906px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 624.5px; margin-bottom: -17px; border-right-width: 13px; min-height: 45px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 405.906px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">sklearn</span>.<span class="cm-property">model_selection</span> <span class="cm-keyword">import</span> <span class="cm-variable">train_test_split</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">x_train</span>,<span class="cm-variable">x_test</span>,<span class="cm-variable">y_train</span>,<span class="cm-variable">y_test</span><span class="cm-operator">=</span><span class="cm-variable">train_test_split</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y</span>,<span class="cm-variable">test_size</span><span class="cm-operator">=</span><span class="cm-number">0.2</span>,<span class="cm-variable">random_state</span><span class="cm-operator">=</span><span class="cm-number">0</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 45px;"></div><div class="CodeMirror-gutters" style="display: none; height: 58px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[29]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 56.5938px; left: 51.7969px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="false"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 162.594px; margin-bottom: -17px; border-right-width: 13px; min-height: 79px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 51.7969px; top: 51px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">x_train</span>.<span class="cm-property">shape</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">y_train</span>.<span class="cm-property">shape</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">x_test</span>.<span class="cm-property">shape</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span><span class=" CodeMirror-matchingbracket">(</span><span class="cm-variable">y_test</span>.<span class="cm-property">shape</span><span class=" CodeMirror-matchingbracket">)</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 79px;"></div><div class="CodeMirror-gutters" style="display: none; height: 92px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>(20, 1)
(20,)
(5, 1)
(5,)
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[30]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 22.5938px; left: 5.59375px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 393.516px; margin-bottom: -17px; border-right-width: 13px; min-height: 62px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 5.59375px; top: 17px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">sklearn</span>.<span class="cm-property">linear_model</span> <span class="cm-keyword">import</span> <span class="cm-variable">LinearRegression</span> </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">regressor</span> <span class="cm-operator">=</span> <span class="cm-variable">LinearRegression</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">regressor</span>.<span class="cm-property">fit</span>(<span class="cm-variable">x_train</span>,<span class="cm-variable">y_train</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 62px;"></div><div class="CodeMirror-gutters" style="display: none; height: 75px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[30]:</bdi></div><div class="output_subarea output_text output_result"><pre>LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[31]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 213.469px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 216.469px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 213.469px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span><span class=" CodeMirror-matchingbracket">(</span><span class="cm-variable">regressor</span>.<span class="cm-property">intercept_</span><span class=" CodeMirror-matchingbracket">)</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>2.018160041434683
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[32]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 174.984px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 177.984px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 174.984px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span><span class=" CodeMirror-matchingbracket">(</span><span class="cm-variable">regressor</span>.<span class="cm-property">coef_</span><span class=" CodeMirror-matchingbracket">)</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>[9.91065648]
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[36]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 22.5938px; left: 21px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="false"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 586.016px; margin-bottom: -17px; border-right-width: 13px; min-height: 45px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 21px; top: 17px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">df</span> <span class="cm-operator">=</span> <span class="cm-variable">pd</span>.<span class="cm-property">DataFrame</span>({<span class="cm-string">'Actual'</span>:<span class="cm-variable">y_test</span>.<span class="cm-property">flatten</span>(),<span class="cm-string">'Predicted'</span>:<span class="cm-variable">y_pred</span>.<span class="cm-property">flatten</span>()})</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">df</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 45px;"></div><div class="CodeMirror-gutters" style="display: none; height: 58px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[36]:</bdi></div><div class="output_subarea output_html rendered_html output_result"><div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Actual</th>
      <th>Predicted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>16.884145</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>33.732261</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69</td>
      <td>75.357018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>26.794801</td>
    </tr>
    <tr>
      <th>4</th>
      <td>62</td>
      <td>60.491033</td>
    </tr>
  </tbody>
</table>
</div></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[42]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 22.5938px; left: 359.766px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 370.469px; margin-bottom: -17px; border-right-width: 13px; min-height: 62px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 359.766px; top: 17px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">scatter</span>(<span class="cm-variable">x_test</span>,<span class="cm-variable">y_test</span>,<span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'blue'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span><span class=" CodeMirror-matchingbracket">(</span><span class="cm-variable">x_test</span>,<span class="cm-variable">y_pred</span>,<span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'red'</span>,<span class="cm-variable">linewidth</span><span class="cm-operator">=</span><span class="cm-number">2</span><span class=" CodeMirror-matchingbracket">)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">show</span>()</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 62px;"></div><div class="CodeMirror-gutters" style="display: none; height: 75px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[48]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 56.5938px; left: 667.703px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 670.703px; margin-bottom: -17px; border-right-width: 13px; min-height: 79px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 667.703px; top: 51px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">sklearn</span> <span class="cm-keyword">import</span> <span class="cm-variable">metrics</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">'Mean Absolute Error:'</span>,<span class="cm-variable">metrics</span>.<span class="cm-property">mean_absolute_error</span>(<span class="cm-variable">y_test</span>,<span class="cm-variable">y_pred</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">'Mean Squared Error:'</span>,<span class="cm-variable">metrics</span>.<span class="cm-property">mean_squared_error</span>(<span class="cm-variable">y_test</span>,<span class="cm-variable">y_pred</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span><span class=" CodeMirror-matchingbracket">(</span><span class="cm-string">'Root Mean Squared Error:'</span>, <span class="cm-variable">np</span>.<span class="cm-property">sqrt</span>(<span class="cm-variable">metrics</span>.<span class="cm-property">mean_squared_error</span>(<span class="cm-variable">y_test</span>, <span class="cm-variable">y_pred</span>))<span class=" CodeMirror-matchingbracket">)</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 79px;"></div><div class="CodeMirror-gutters" style="display: none; height: 92px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>Mean Absolute Error: 4.183859899002975
Mean Squared Error: 21.5987693072174
Root Mean Squared Error: 4.6474476121003665
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 5.59375px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 8.59375px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 5.59375px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="display:none"><div class="tooltipbuttons"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">Close</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="ui-corner-all" role="button" id="expanbutton" title="Grow the tooltip vertically (press shift-tab twice)"><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button" title="show the current docstring in pager (press shift-tab 4 times)"><span class="ui-icon ui-icon-arrowstop-l-n">Open in Pager</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button" title="Tooltip will linger for 10 seconds while you type" style="display: none;"><span class="ui-icon ui-icon-clock">Close</span></a></div><div class="pretooltiparrow"></div><div class="tooltiptext smalltooltip"></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="Open the pager in an external window" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="Close the pager" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "5.7.8", "notebook_path": "C:\\Users\\aparn\\aparna\\anaconda\\lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]", "sys_executable": "C:\\Users\\aparn\\aparna\\anaconda\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.18362-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="./task2_files/encoding.js.download" charset="utf-8"></script>

<script src="./task2_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div></body></html>