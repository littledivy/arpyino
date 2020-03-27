from distutils.core import setup
setup(
  name = 'arpyino',
  packages = ['arpyino'],
  version = '0.1',
  license='MIT',
  description = 'A simple wrapper around the serial library to communicate with the Arduino board.',
  author = 'Divy Srivastava',
  author_email = 'dj.srivastava23@gmail.com',
  url = 'https://github.com/divy-work/arpyino',
  download_url = 'https://github.com/divy-work/arpyino/archive/v_01.tar.gz',
  keywords = ['serial', 'arduino', 'serial-port', 'arduino-read', 'communicate-with-arduino'],
  install_requires=[
          'pyserial'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
