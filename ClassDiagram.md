```mermaid
classDiagram
	direction TB
	class Config {
		fileAssociations : dict[str, FileTypeDescriptor]
		columns : list[PropertyFormatter]
	}
	class Application {
		context : AppContext
		tui : TUI
	}
	class AppContext {
		currentPath : str
		items: list[Item]
	}
	class TUI {
		display(context : AppContext)
	}
	class PopupTUI {
		display(appContext : AppContext, popupContext : PopupContext)
	}
	class ContentTUI {
		display(context : AppContext)
	}
	class ListContentTUI {
		display(context : AppContext)
	}
	
	class TileContentTUI {
		display(context : AppContext)
	}
	
	class BigListContentTUI {
		display(context : AppContext)
	}
	class Item {
		path : str
		name : str
	}
	class File {
		extension : str
		size : int
		modifiedTime : int
		createdTime : int
		descriptor : FileTypeDescriptor
	}
	
	class Directory {
		items : int
	}
	class PropertyFormatter {
		name : str
		format(item : Item) str
	}
	class HybridFormatter {
		fFormatter : PropertyFormatter
		dFormatter : PropertyFormatter
		format(item : Item) 
	}
	class FileTypeDescriptor {
		canonicalName : str
		operations : list[FileOperation]
	}
	
	class FileOperation {
		description : str
		execute(path : str)
	}
	Application "1" *-- "1" AppContext
	Application "1" *-- "1" TUI
	Application ..> Config

	AppContext "1" o-- "*" Item
	Item <|-- File
	Item <|-- Directory

	Config "1" o-- "*" FileTypeDescriptor
	Config <.. TUI
	Config "1" o-- "*" PropertyFormatter

	PropertyFormatter <|-- HybridFormatter
	PropertyFormatter <|-- NameFormatter
	PropertyFormatter <|-- Base2SizeFormatter
	PropertyFormatter <|-- TimeFormatter	
	TimeFormatter <|-- ModifiedTimeFormatter
	TimeFormatter <|-- CreatedTimeFormatter
	PropertyFormatter <|-- Base10SizeFormatter	

	TUI "1" *-- "1" ContentTUI
	TUI "1" *-- "1" PopupTUI
	ContentTUI <|-- ListContentTUI
	ContentTUI <|-- TileContentTUI
	ContentTUI <|-- BigListContentTUI

	TUI ..> PyTermGUI
	
	FileTypeDescriptor "*" o-- "*" FileOperation
	File "*" o-- "1" FileTypeDescriptor
	
	FileOperation ..> TUI
```

