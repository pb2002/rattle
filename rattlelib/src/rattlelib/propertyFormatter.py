from abc import abstractmethod
from dataclasses import dataclass
import math
from typing import Generic, TypeVar
from item import Item, File, Directory

T = TypeVar('T')
class IFormatter(Generic[T]):
    @abstractmethod
    def format(self, t: T) -> str:
        raise NotImplementedError()

FileFormatter = IFormatter[File]               
DirectoryFormatter = IFormatter[Directory]
        
class _EmptyFileFormatter(FileFormatter):
    def format(self, file: File) -> str: return ""

class _EmptyDirectoryFormatter(DirectoryFormatter):
    def format(self, dir: Directory) -> str: return ""

@dataclass
class PropertyFormatter(IFormatter[Item]):
    name: str
    fileFormatter: FileFormatter = _EmptyFileFormatter()
    dirFormatter: DirectoryFormatter = _EmptyDirectoryFormatter()

    def format(self, item: Item) -> str:
        if (isinstance(item, File)): 
            return self.fileFormatter.format(item)
        return self.dirFormatter.format(item)

class Base10SizeFormatter(FileFormatter):
    _sizeUnits10 = ["B","KB","MB","GB","TB","PB","EB","ZB","YB"]
    
    def format(self, file: File) -> str:
        
        if (file.size == 0): 
            return "0 B"

        mag = math.log10(file.size) // 3
        return f"{file.size / (10 ** (mag * 3))} {self._sizeUnits10[mag]}"

class Base2SizeFormatter(FileFormatter):
    _sizeUnits2 = ["B","KiB","MiB","GiB","TiB","PiB","EiB","ZiB","YiB"]

    def format(self, file: File) -> str:
        if (file.size == 0): 
            return "0 B"
        mag = math.log2(file.size) // 10
        return f"{file.size / (10 ** (mag * 10))} {self._sizeUnits2[mag]}"

class Log2SizeFormatter(FileFormatter): 
    def format(self, file: File) -> str: return f"{0 if file.size == 0 else math.log2(file.size)}"

class Log10SizeFormatter(PropertyFormatter): 
    def format(self, file: File) -> str: return f"{0 if file.size == 0 else math.log10(file.size)}"

class NyaSizeFormatter(PropertyFormatter):
    _sizeNya = [
        "nya",
        "big nya",
        "mega nya",
        "sugoi nya",
        "nyaaaaa",
        "nyaaaaaa",
        "nyaaaaaaa",
        "nyaaaaaaaa",
        "nyaaaaaaaaa"
    ]
    def format(self, file: File) -> str:
        if (file == 0): 
            return "ewmpti T.T"
        mag = math.log2(file) // 10
        return f"{file / (10 ** (mag * 10))} {self._sizeNya[mag]}"