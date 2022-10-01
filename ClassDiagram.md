```mermaid
classDiagram
	direction LR
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

	Application ..> Config
	Config "1" o-- "*" FileTypeDescriptor
	Config "1" o-- "*" PropertyFormatter
	Config <.. TUI

	AppContext "1" o-- "*" Item
	Item <|-- File
	Item <|-- Directory

	PropertyFormatter <|-- NameFormatter
	PropertyFormatter <|-- TimeFormatter	
	TimeFormatter <|-- ModifiedTimeFormatter
	TimeFormatter <|-- CreatedTimeFormatter
	PropertyFormatter <|-- Base2SizeFormatter
	PropertyFormatter <|-- Base10SizeFormatter	
	PropertyFormatter <|-- HybridFormatter

	Application "1" *-- "1" TUI
	TUI ..> PyTermGUI
	TUI "1" *-- "1" ContentTUI
	ContentTUI <|-- ListContentTUI
	ContentTUI <|-- TileContentTUI
	ContentTUI <|-- BigListContentTUI
	TUI "1" *-- "1" PopupTUI

	
	FileTypeDescriptor "*" o-- "*" FileOperation
	File "*" o-- "1" FileTypeDescriptor
	
```

