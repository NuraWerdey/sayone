import os
import importlib.util

def load_all_modules(client):
    modules_dir = "modules"
    if not os.path.exists(modules_dir):
        os.makedirs(modules_dir)
        return
    
    for file in os.listdir(modules_dir):
        if file.endswith(".py") and not file.startswith("_"):
            module_name = file[:-3]  # Deleting .py
            module_path = os.path.join(modules_dir, file)
            
            # Import 
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            
            if hasattr(module, "setup"):
                module.setup(client)
                print(f"✅ Модуль {module_name} загружен!")
                
RESTRICTED_BUILTINS = ["eval", "exec", "open", "__import__"]

spec.loader.exec_module(module)
module.__dict__["__builtins__"] = {
    k: v for k, v in __builtins__.items() 
    if k not in RESTRICTED_BUILTINS
}                
