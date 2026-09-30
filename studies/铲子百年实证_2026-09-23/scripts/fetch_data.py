# Compatibility entry; original implementation archived in archive/v1/scripts.
import pathlib
import runpy

if __name__ == '__main__':
    runpy.run_path(str(pathlib.Path(__file__).with_name('fetch_audit_data.py')), run_name='__main__')
