from app import app, db, Project

def view_all_projects():
    with app.app_context():
        projects = Project.query.all()
        if not projects:
            print("\nNo projects found.")
        else:
            print("\n=== All Projects ===")
            for p in projects:
                print(f"\nID: {p.id}")
                print(f"Title: {p.title}")
                print(f"Description: {p.description}")
                print(f"Technologies: {p.technologies}")
                print(f"GitHub: {p.github_url}")
                print(f"Live URL: {p.live_url}")
                print("-" * 50)

def add_project():
    with app.app_context():
        print("\n=== Add New Project ===\n")
        
        title = input("Title: ")
        description = input("Description: ")
        technologies = input("Technologies (comma separated): ")
        github_url = input("GitHub URL (optional): ")
        live_url = input("Live URL (optional): ")
        image_url = input("Image URL (optional): ")
        
        new_project = Project(
            title=title,
            description=description,
            technologies=technologies if technologies else None,
            github_url=github_url if github_url else None,
            live_url=live_url if live_url else None,
            image_url=image_url if image_url else None
        )
        
        try:
            db.session.add(new_project)
            db.session.commit()
            print(f"\n✓ Project '{title}' added successfully! (ID: {new_project.id})")
        except Exception as e:
            db.session.rollback()
            print(f"\n✗ Error: {e}")

def delete_project():
    with app.app_context():
        projects = Project.query.all()
        if not projects:
            print("\nNo projects to delete.")
            return
        
        print("\n=== Current Projects ===")
        for p in projects:
            print(f"ID {p.id}: {p.title}")
        
        try:
            project_id = int(input("\nEnter project ID to delete: "))
            project = Project.query.get(project_id)
            
            if project:
                confirm = input(f"Delete '{project.title}'? (yes/no): ")
                if confirm.lower() in ['yes', 'y']:
                    db.session.delete(project)
                    db.session.commit()
                    print(f"\n✓ Project deleted successfully!")
                else:
                    print("\nCancelled.")
            else:
                print("\nProject not found.")
        except ValueError:
            print("\nInvalid ID.")
        except Exception as e:
            db.session.rollback()
            print(f"\n✗ Error: {e}")

def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("PROJECT DATABASE MANAGER")
        print("=" * 50)
        print("1. Add new project")
        print("2. View all projects")
        print("3. Delete project")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ")
        
        if choice == '1':
            add_project()
        elif choice == '2':
            view_all_projects()
        elif choice == '3':
            delete_project()
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Try again.")

if __name__ == '__main__':
    main_menu()