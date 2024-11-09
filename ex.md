


[![GitHub release (latest by date)](https://img.shields.io/github/v/tag/insality/druid?style=for-the-badge&label=Release)](https://github.com/Insality/druid/tags)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/insality/druid/ci-workflow.yml?branch=master&style=for-the-badge)](https://github.com/Insality/druid/actions)
[![codecov](https://img.shields.io/codecov/c/github/Insality/druid?style=for-the-badge)](https://codecov.io/gh/Insality/druid)

[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/insality) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/insality) [![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/insality)

**Druid** - powerful **Defold** component UI framework that empowers developers to create stunning and customizable GUIs by leveraging a wide range of embedded components or effortlessly designing their own game-specific components.

## Druid Example

Check the [**HTML5 version**](https://insality.github.io/druid/druid/) of the **Druid** example app.

In this example you can inspect a variety of **Druid** components and see how they work. Each example page provides a direct link to the corresponding example code, making it easier for you to understand how to use **Druid**.

## Setup

### Dependency

To integrate the **Druid** extension into your own project, add this project as a [dependency](https://www.defold.com/manuals/libraries/) in your **Defold** game. Open your `game.project` file and add the following line to the dependencies field under the project section:

**Druid v1.0**

> [https://github.com/Insality/druid/archive/refs/tags/1.0.zip](https://github.com/Insality/druid/archive/refs/tags/1.0.zip)

Here is a list of [all releases](https://github.com/Insality/druid/releases).


### Library Size

> **Note:** The library size is calculated based on the build report per platform. The extended components are exlcuded, which are including only on demand.

| Platform         | Library Size  |
| ---------------- | ------------- |
| HTML5            | **38.00 KB**  |
| Desktop / Mobile | **65.74 KB**  |


### Input Bindings

**Druid** utilizes the `/builtins/input/all.input_binding` input bindings. Either use this file for your project by setting the `Runtime -> Input -> Game Binding` field in the `game.project` input section to `/builtins/input/all.input_binding`, or add the specific bindings you need to your game's input binding file. For custom input bindings, refer to the Input Binding section in the [Advanced Setup](https://github.com/Insality/druid/blob/master/docs_md/advanced-setup.md#input-bindings).


## Usage

### Basic usage

To utilize **Druid**, begin by creating a **Druid** instance to instantiate components and include the main functions of **Druid**: *update*, *final*, *on_message*, and *on_input*.

When using **Druid** components, provide a node name string as an argument. If you don't have the node name available in some cases, you can pass `gui.get_node()` instead.

All **Druid** and component methods are invoked using the `:` operator, such as `self.druid:new_button()`.

```lua
local druid = require("druid.druid")

-- All component callbacks pass "self" as first argument
-- This "self" is a context data passed in `druid.new(context)`
local function on_button_callback(self)
    print("The button clicked!")
end

function init(self)
    self.druid = druid.new(self)
    self.button = self.druid:new_button("button_node_name", on_button_callback)
end

-- "final" is a required function for the correct Druid workflow
function final(self)
    self.druid:final()
end

-- "update" is used in progress bar, scroll, and timer basic components
function update(self, dt)
    self.druid:update(dt)
end

-- "on_message" is used for specific Druid events, like language change or layout change
function on_message(self, message_id, message, sender)
    self.druid:on_message(message_id, message, sender)
end

-- "on_input" is used in almost all Druid components
-- The return value from `druid:on_input` is required!
function on_input(self, action_id, action)
    return self.druid:on_input(action_id, action)
end

```

For all **Druid** instance functions, [see here](https://insality.github.io/druid/modules/DruidInstance.html).


### API Documentation

**Druid** offers a wide range of components and functions. To facilitate usage, **Druid** provides comprehensive API documentation with examples and annotations.

Start reading the API documentation [here](https://insality.github.io/druid/modules/Druid.html).

**Druid** provide the *EmmyLua* annotations to add autocomplete inside your IDE. Check [EmmyLua Setup here](docs_md/advanced-setup.md#emmylua-annotations).


### Create custom components

If you want to create your own components, refer to the [Create Custom Components](docs_md/02-creating_custom_components.md) section in the documentation.

Custom components are one of the most powerful features of **Druid**. They allow you to create your own components effortlessly and utilize them in your game.


## Druid Components

Here is full **Druid** components list.

### Basic Components

> Basic components always included in the build and available for use.

| Name | Description | Example | <div style="width:200px">Preview</div> |
|------|-------------|---------|---------|
| **[Button](https://insality.github.io/druid/modules/Button.html)** | Logic over GUI Node. Handle the user click interactions: click, long click, double click, etc. | [Button Example](https://insality.github.io/druid/druid/?example=general_buttons) | <img src="media/preview/button.gif" width="200" height="100"> |
| **[Text](https://insality.github.io/druid/modules/Text.html)** | Logic over GUI Text. By default Text component fit the text inside text node size area with different adjust modes. | [Text Example](https://insality.github.io/druid/druid/?example=texts_general) | <img src="media/preview/text.gif" width="200" height="100"> |
| **[Scroll](https://insality.github.io/druid/modules/Scroll.html)** | Logic over two GUI Nodes: input and content. Provides basic behaviour for scrollable content. | [Scroll Example](https://insality.github.io/druid/druid/?example=general_scroll) | <img src="media/preview/scroll.gif" width="200" height="100"> |
| **[Blocker](https://insality.github.io/druid/modules/Blocker.html)** | Logic over GUI Node. Don't pass any user input below node area size. | [Blocker Example](https://insality.github.io/druid/druid/?example=timer) | <img src="media/preview/blocker.gif" width="200" height="100"> |
| **[Back Handler](https://insality.github.io/druid/modules/BackHandler.html)** | Call callback on user "Back" action. It's a Android back button or keyboard backspace key | [Back Handler Example](https://insality.github.io/druid/druid/?example=timer) | <img src="media/preview/back_handler.gif" width="200" height="100"> |
| **[Static Grid](https://insality.github.io/druid/modules/StaticGrid.html)** | Logic over GUI Node. Component to manage node positions with all equal node sizes. | [Static Gid Example](https://insality.github.io/druid/druid/?example=general_grid) | <img src="media/preview/static_grid.gif" width="200" height="100"> |
| **[Hover](https://insality.github.io/druid/modules/Hover.html)** | Logic over GUI Node. Handle hover action over node. For both: mobile touch and mouse cursor. | [Hover Example](https://insality.github.io/druid/druid/?example=timer) | <img src="media/preview/hover.gif" width="200" height="100"> |
| **[Swipe](https://insality.github.io/druid/modules/Swipe.html)** | Logic over GUI Node. Handle swipe gestures over node. | [Swipe Example](https://insality.github.io/druid/druid/?example=general_swipe) | <img src="media/preview/swipe.gif" width="200" height="100"> |
| **[Drag](https://insality.github.io/druid/modules/Drag.html)** | Logic over GUI Node. Handle drag input actions. Can be useful to make on screen controlls. | [Drag Example](https://insality.github.io/druid/druid/?example=general_drag) | <img src="media/preview/drag.gif" width="200" height="100"> |


### Extended components

> Extended components before usage should be registered in **Druid** with [`druid.register()`](https://insality.github.io/druid/modules/Druid.html#druid.register) function.
> On usage of unregistered **Druid** component the next log will be shown in the console.
```
local data_list = require("druid.extended.data_list")
druid.register("data_list", data_list)
```

| Name | Description | Example | <div style="width:200px">Preview</div> |
|------|-------------|---------|---------|
| **[Data List](https://insality.github.io/druid/modules/DataList.html)** | Logic over Scroll and Grid components. Create only visible GUI nodes or components to make "infinity" scroll befaviour | [Data List Example](https://insality.github.io/druid/druid/?example=general_data_list) | <img src="media/preview/data_list.gif" width="200" height="100"> |
| **[Input](https://insality.github.io/druid/modules/Input.html)** | Logic over GUI Node and GUI Text (or Text component). Provides basic user text input. | [Input Example](https://insality.github.io/druid/druid/?example=general_input) | <img src="media/preview/input.gif" width="200" height="100"> |
| **[Lang text](https://insality.github.io/druid/modules/LangText.html)** | Logic over Text component to handle localization. Can be translated in real-time with `druid.on_language_change` | [Lang Text Example](https://insality.github.io/druid/druid/?example=timer) | <img src="media/preview/lang_text.gif" width="200" height="100"> |
| **[Progress](https://insality.github.io/druid/modules/Progress.html)** | Logic over GUI Node. Handle node size and scale to handle progress node size. | [Progress Example](https://insality.github.io/druid/druid/?example=general_progress_bar) | <img src="media/preview/progress.gif" width="200" height="100"> |
| **[Slider](https://insality.github.io/druid/modules/Slider.html)** | Logic over GUI Node. Handle draggable node with position restrictions. | [Slider Example](https://insality.github.io/druid/druid/?example=general_sliders) | <img src="media/preview/slider.gif" width="200" height="100"> |
| **[Timer](https://insality.github.io/druid/modules/Timer.html)** | Logic over GUI Text. Handle basic timer functions. | [Timer Example](https://insality.github.io/druid/druid/?example=timer) | <img src="media/preview/timer.gif" width="200" height="100"> |
| **[Hotkey](https://insality.github.io/druid/modules/Hotkey.html)** | Allow to set callbacks for keyboard hotkeys with key modificators. | [Hotkey Example](https://insality.github.io/druid/druid/?example=general_hotkey) | <img src="media/preview/hotkey.gif" width="200" height="100"> |
| **[Layout](https://insality.github.io/druid/modules/Layout.html)** | Logic over GUI Node. Arrange nodes inside layout node with margin/paddings settings. | [Layout Example](https://insality.github.io/druid/druid/?example=general_layout) | <img src="media/preview/layout.gif" width="200" height="100"> |
| **[Rich Input](https://insality.github.io/druid/modules/RichInput.html)** | Logic over GUI Node and GUI Text (or Text component). Provides rich text input with different styles and text formatting. | [Rich Input Example](https://insality.github.io/druid/druid/?example=general_rich_input) | <img src="media/preview/rich_input.gif" width="200" height="100"> |
| **[Rich Text](https://insality.github.io/druid/modules/RichText.html)** | Logic over GUI Text. Provides rich text formatting with different styles and text formatting. | [Rich Text Example](https://insality.github.io/druid/druid/?example=general_rich_text) | <img src="media/preview/rich_text.gif" width="200" height="100"> |

For a complete overview, see: **_[components.md](docs_md/01-components.md)_**.


## Druid Events

Any **Druid** components as callbacks use [Druid Events](https://insality.github.io/druid/modules/DruidEvent.html). In component API ([button example](https://insality.github.io/druid/modules/Button.html#on_click)) pointed list of component events. You can manually subscribe to these events with the following API:

- **event:subscribe**(callback)

- **event:unsubscribe**(callback)

- **event:clear**()

You can subscribe several callbacks to a single event.

## Details

- **Druid** processes input in a stack-based manner. The most recently created button will be checked first. Create your input GUI components from back to front.
- Remember to include `return` in the `on_input` function: `return self.druid:on_input()`. This is necessary if you have multiple input sources (multiple Druid instances, other input systems, etc.).
- Druid automatically calls `acquire_input_focus` if you have input components. Therefore, manual calling of `acquire_input_focus` is not required.
- When deleting a **Druid** component node, make sure to remove it using `druid:remove(component)`.


## Examples

Try the [**HTML5 version**](https://insality.github.io/druid/druid/) of the **Druid** example app.

Each example page provides a direct link to the corresponding example code, making it easier for you to understand how to use **Druid**.

Or refer directly to the [**example folder**](https://github.com/Insality/druid/tree/develop/example) for code examples demonstrating how to use **Druid**.

## Documentation

To better understand **Druid**, read the following documentation:
- [How To GUI in Defold](https://forum.defold.com/t/how-to-gui-in-defold/73256)
- [Druid components](docs_md/01-components.md)
- [Create custom components](docs_md/02-creating_custom_components.md)
- [See FAQ article](docs_md/FAQ.md)
- [Druid styles](docs_md/03-styles.md)

You can find the full **Druid** [documentation here](https://insality.github.io/druid/modules/Druid.html).


## Licenses

- Developed and supported by [Insality](https://github.com/Insality)
- Original idea by [AGulev](https://github.com/AGulev)
- Assets from [Kenney](http://www.kenney.nl/)


## Issues and suggestions

If you have any issues, questions or suggestions please [create an issue](https://github.com/Insality/druid/issues) or contact me: [insality@gmail.com](mailto:insality@gmail.com)


## History
For a complete history of the development of **Druid**, please check the [changelog](docs_md/changelog.md).


## 👏 Contributors

<a href="https://github.com/Insality/druid/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=insality/druid"/>
</a>


## ❤️ Support project ❤️

Your donation helps me stay engaged in creating valuable projects for **Defold**. If you appreciate what I'm doing, please consider supporting me!

[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/insality) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/insality) [![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/insality)