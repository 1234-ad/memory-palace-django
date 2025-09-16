# 🧠 Memory Palace Django App

A modern web application that implements the ancient **Method of Loci** (Memory Palace technique) to help users dramatically improve their memory retention and recall abilities.

## 🌟 Features

### Core Functionality
- **Create Memory Palaces**: Build virtual representations of familiar locations
- **Room Management**: Organize your palace into logical rooms and spaces
- **Memory Items**: Place information you want to remember in specific locations
- **Study Sessions**: Practice recall with built-in spaced repetition
- **Progress Tracking**: Monitor your mastery of different memory items
- **Visual Learning**: Upload images for palaces, rooms, and memory items

### User Experience
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Intuitive Interface**: Clean, modern UI built with Bootstrap 5
- **User Authentication**: Secure registration, login, and profile management
- **Interactive Study Mode**: Gamified learning experience with progress tracking

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/1234-ad/memory-palace-django.git
   cd memory-palace-django
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   Open your browser and go to `http://127.0.0.1:8000`

## 📖 How to Use

### 1. Create Your First Memory Palace
- Sign up for an account or log in
- Click "Create New Palace"
- Choose a familiar location (your home, school, workplace)
- Add a description and optional image

### 2. Add Rooms
- Navigate to your palace
- Add rooms in the order you would naturally walk through them
- Include descriptions and images to make them more memorable

### 3. Place Memory Items
- Enter each room
- Add items you want to remember
- Use vivid, unusual associations
- Include mnemonic hints to strengthen recall

### 4. Study and Practice
- Start a study session
- Walk through your palace mentally
- Test your recall of each memory item
- Mark items as "mastered" when you've learned them

## 🏗️ Project Structure

```
memory-palace-django/
├── memory_palace/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── palaces/               # Core app for memory palaces
│   ├── models.py         # Palace, Room, MemoryItem, StudySession
│   ├── views.py          # All palace-related views
│   ├── forms.py          # Forms for creating/editing
│   ├── urls.py           # URL patterns
│   └── admin.py          # Admin interface
├── accounts/             # User authentication
│   ├── views.py
│   └── urls.py
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── palaces/
│   └── registration/
├── static/              # CSS, JS, images
├── media/               # User uploads
└── requirements.txt     # Python dependencies
```

## 🎯 Key Models

### Palace
- User's memory palace with name, description, type, and image
- Can be public or private
- Tracks creation and modification dates

### Room
- Individual rooms within a palace
- Ordered sequence for logical navigation
- Coordinates for visual layout
- Associated images for better recall

### MemoryItem
- Information to be remembered
- Categorized by type (text, number, name, etc.)
- Includes mnemonic hints and mastery status
- Positioned within specific rooms

### StudySession
- Tracks practice sessions
- Records accuracy and progress
- Implements spaced repetition principles

## 🎨 Design Philosophy

### Memory Science
- Based on the 2,500-year-old Method of Loci
- Leverages spatial memory and visual associations
- Implements proven cognitive science principles

### User Experience
- Intuitive, distraction-free interface
- Progressive disclosure of complexity
- Gamification elements to encourage practice
- Mobile-first responsive design

### Technical Excellence
- Clean, maintainable Django code
- Comprehensive admin interface
- Scalable database design
- Security best practices

## 🔧 Advanced Features

### Admin Interface
- Comprehensive management of all models
- User analytics and progress tracking
- Content moderation tools
- System monitoring capabilities

### API Ready
- Models designed for future API expansion
- UUID primary keys for security
- Structured data relationships

### Extensibility
- Plugin-ready architecture
- Custom palace types
- Flexible memory item categories
- Expandable study session analytics

## 🚀 Deployment

### Environment Variables
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
```

### Static Files
```bash
python manage.py collectstatic
```

### Database
- SQLite for development
- PostgreSQL recommended for production
- Automatic migrations included

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

### Memory Palace Technique
- [Method of Loci - Wikipedia](https://en.wikipedia.org/wiki/Method_of_loci)
- [Memory Palace Technique Guide](https://artofmemory.com/wiki/Method_of_Loci)
- [Scientific Research on Spatial Memory](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3866350/)

### Django Development
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Ancient Greek and Roman orators who developed the Method of Loci
- Modern memory champions who keep the technique alive
- The Django community for excellent documentation and tools
- Bootstrap team for the responsive framework

## 📞 Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Check the wiki for detailed documentation

---

**Built with ❤️ using Django and the power of spatial memory**