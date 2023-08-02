# Pyventor: Dynamic Event Handling in Python
eventListener provides a flexible and robust event management system tailored for Python applications. It allows developers to define custom events, register callback functions for those events, and trigger them as needed, all while maintaining execution priority. The system is designed with ease of use and extensibility in mind, making it ideal for applications that require dynamic interactions or custom workflows.

## Features:
* **Custom Event Registration:** Easily define and manage custom events using the addEvent method.
* **Prioritized Callback Execution:** Register callback functions with different priorities to control the order of their execution.
* **Dynamic Event Triggering:** Trigger custom events with any number of arguments.
* **Intuitive Error Handling:** Clear and descriptive error messages help developers diagnose and fix issues quickly.

## Function Descriptions:
### `addEvent(event_name: str) -> bool:`

* **Purpose**: Registers a new custom event.
* **Parameters**:
  - `event_name`: The name of the event to be registered.

* **Returns**: `True` if the event is successfully added, `False` if it already exists.
  
### `add_event_listener(event_name: str, callback: Callable, priority: str = "normal") -> bool:`

* **Purpose**: Registers a callback function for a specific event with a given priority.
* **Parameters**:
  - `event_name`: The name of the event to attach the callback to.
  - `callback`: The function to be called when the event is triggered.
  - `priority`: (Optional) The execution priority of the callback. Can be "high", "normal", "low", or with added granularity like "high+1", "low-2", etc.

* **Returns**: `True` if the callback is successfully added, False otherwise (e.g., if the callback is already added).
  
### `trigger_event(event_name: str, *args, kwargs) -> None:`

* **Purpose**: Triggers a specific event, leading to the execution of all registered callback functions in order of their priority.
* **Parameters**:
- `event_name`: The name of the event to be triggered.
- `*args`: Variable positional arguments passed to the callback functions.
- `**kwargs`: Variable keyword arguments passed to the callback functions.

### `isEventHandlerAdded(event_name: str, callback: Callable) -> bool:`

* **Purpose:** Checks if a specific callback function is already registered for a given event.
* **Parameters:**
- `event_name`: The name of the event.
- `callback`: The callback function to check.
* **Returns**: `True` if the callback is already registered for the event, `False` otherwise.

### `removeEventHandler(event_name: str, callback: Callable) -> bool:`

* **Purpose:** Removes a registered callback function from a specific event.
* **Parameters:**
- `event_name`: The name of the event.
- `callback`: The callback function to be removed.
* **Returns:** `True` if the callback is successfully removed, `False` otherwise (e.g., if the callback wasn't registered in the first place).
This description provides a comprehensive overview of the library, its main features, and detailed explanations of each function. It can serve as an introductory guide for potential users or contributors.
