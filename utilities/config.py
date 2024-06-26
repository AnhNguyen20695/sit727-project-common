APP_DATABASE = "workflow_app"

HOST_CONFIG = {
    'dev': {
        'DATABASE': {
            'primary': {
                'HOST': 'mysql-0.mysql.default.svc.cluster.local',
                'PORT': 3306,
                'USER': 'root',
                'PASSWORD': 'admin',
            },
            'read': {
                'HOST': 'mysql-0.mysql.default.svc.cluster.local',
                'PORT': 3306,
                'USER': 'root',
                'PASSWORD': 'admin',
            }
        },
        'NOTE_HOST': 'localhost',
        'NOTE_PORT': 5001
    },
    'prod': {
        'DATABASE': {
            'primary': {
                'HOST': 'mysql-0.mysql.default.svc.cluster.local',
                'PORT': 3306,
                'USER': 'root',
                'PASSWORD': 'admin',
            },
            'read': {
                'HOST': 'mysql-0.mysql.default.svc.cluster.local',
                'PORT': 3306,
                'USER': 'root',
                'PASSWORD': 'admin',
            }
        },
        'NOTE_HOST': 'note-microservice',
        'NOTE_PORT': 5001
    }
}
