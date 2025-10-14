use godot::prelude::*;
use chrono::Local;

#[derive(GodotClass)]
#[class(base = RefCounted)]
pub struct AppLogger {
    base: Base<RefCounted>,
    name: GString,
}

#[godot_api]
impl IRefCounted for AppLogger {
    fn init(base: Base<RefCounted>) -> Self {
        Self {
            base,
            name: "VLogger".into(),
        }
    }
}

#[godot_api]
impl AppLogger {
    

    #[func]
    pub fn create(name: GString) -> Gd<Self> {
        Gd::from_init_fn(|base| Self {
            base,
            name: name.clone(),
        })
    }

    #[func]
    pub fn set_name(&mut self, name: GString) {
        self.name = name;
    }

    #[func]
    pub fn info(&self, msg: GString) {
        let now = Local::now().format("%Y-%m-%d %H:%M:%S");
        godot_print!("[INFO][{}][{}]: {}", now, self.name, msg);
    }

    #[func]
    pub fn warn(&self, msg: GString) {
        let now = Local::now().format("%Y-%m-%d %H:%M:%S");
        godot_warn!("[WARN][{}][{}]: {}", now, self.name, msg);
    }

    #[func]
    pub fn error(&self, msg: GString) {
        let now = Local::now().format("%Y-%m-%d %H:%M:%S");
        godot_error!("[ERROR][{}][{}]: {}", now, self.name, msg);
    }

    #[func]
    pub fn debug(&self, msg: GString) {
        let now = Local::now().format("%Y-%m-%d %H:%M:%S");
        godot_print!("[DEBUG][{}][{}]: {}", now, self.name, msg);
    }

    #[func]
    pub fn global(source: GString, msg: GString) {
        let now = Local::now().format("%Y-%m-%d %H:%M:%S");
        godot_print!("[GLOBAL][{}][{}]: {}", now, source, msg);
    }
}
