import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
            print("📝 Starting with empty task list")
        except json.JSONDecodeError:
            self.tasks = []
            print("⚠️  Corrupted task file, starting fresh")
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")
    
    def add_task(self, description, priority='medium'):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {description}")
    
    def list_tasks(self, show_completed=False):
        """List all tasks"""
        if not self.tasks:
            print("📋 No tasks yet!")
            return
        
        print("\n" + "="*60)
        print("YOUR TASKS")
        print("="*60)
        
        for task in self.tasks:
            if not show_completed and task['completed']:
                continue
            
            status = "✅" if task['completed'] else "⬜"
            priority_icon = {
                'high': '🔴',
                'medium': '🟡',
                'low': '🟢'
            }.get(task['priority'], '⚪')
            
            print(f"{status} [{task['id']}] {priority_icon} {task['description']}")
            print(f"   Created: {task['created_at']}")
        
        print("="*60)
    
    def complete_task(self, task_id):
        """Mark task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✅ Completed: {task['description']}")
                return
        print(f"❌ Task {task_id} not found")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                self.save_tasks()
                print(f"🗑️  Deleted: {deleted['description']}")
                return
        print(f"❌ Task {task_id} not found")

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Show all (including completed)")
        print("6. Exit")
        
        choice = input("\nChoice: ")
        
        try:
            if choice == '1':
                desc = input("Task description: ")
                print("Priority: high, medium, low")
                priority = input("Priority (default: medium): ").lower() or 'medium'
                manager.add_task(desc, priority)
            
            elif choice == '2':
                manager.list_tasks()
            
            elif choice == '3':
                task_id = int(input("Task ID to complete: "))
                manager.complete_task(task_id)
            
            elif choice == '4':
                task_id = int(input("Task ID to delete: "))
                manager.delete_task(task_id)
            
            elif choice == '5':
                manager.list_tasks(show_completed=True)
            
            elif choice == '6':
                print("👋 Goodbye!")
                break
        
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()