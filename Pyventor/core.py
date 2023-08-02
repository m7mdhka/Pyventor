from typing import Callable
import re
import inspect

class eventListener:
    def __init__(self) -> None:
        self.listeners = {}
        self.events = set()

    def addEvent(self, event_name:str) -> bool:
        if event_name not in self.events:
            self.events.add(event_name)
            return True
        return False

    def _determine_priority(self, priority_str:str) -> int:
        base_priority = {
            "high": 1000,
            "normal": 0,
            "low": -1000
        }
        if not re.match(r'^(high|normal|low)([+-]\d+)?$', priority_str):
            print(f"Error: Invalid priority string '{priority_str}'. Using 'normal' priority.")
            return base_priority["normal"]
        
        parts = re.split('[+-]', priority_str)
        offset = (int(parts[1]) if len(parts) > 1 else 0) * -1 if '-' in priority_str else 1
        return base_priority.get(parts[0], 0) + offset

    def add_event_listener(self, event_name:str, callback:Callable, priority:str="normal") -> bool:
        if not callable(callback):
            print("Error: Provided callback is not callable(function).")
            return False
        
        if event_name not in self.events:
            print(f"Error: Event '{event_name}' not defined. Use addEvent() to define it first.")
            return False

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        if any(cb == callback for cb, priority in self.listeners[event_name]):
            print(f"Warning: This callback is already added for the event '{event_name}'. Skipping.")
            return False

        self.listeners[event_name].append((callback, self._determine_priority(priority)))
        return True

    def trigger_event(self, event_name:str, *args, **kwargs) -> None:
        if event_name not in self.listeners:
            print(f"Warning: No listeners registered for event '{event_name}'.")
            return
        
        sorted_listeners = sorted(self.listeners.get(event_name, []), key=lambda x: x[1], reverse=True)
        for callback, priority in sorted_listeners:
            params = inspect.signature(callback).parameters
            required_args = len(params)
            if required_args <= len(args):
                callback(*args[:required_args])
            else:
                callback(*args, **kwargs)

    def isEventHandlerAdded(self, event_name:str, callback:Callable) -> bool:
        return any(cb[0] == callback for cb in self.listeners.get(event_name, []))

    def removeEventHandler(self, event_name:str, callback:Callable) -> bool:
        if event_name in self.listeners:
            original_length = len(self.listeners[event_name])
            self.listeners[event_name] = [cb for cb in self.listeners[event_name] if cb[0] != callback]
            return original_length != len(self.listeners[event_name])
        return False