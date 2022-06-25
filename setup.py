import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="jogo.py", icon="resources/icon.ico"
)]


cx_Freeze.setup(
    name="Comet SpaceShip",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["resources"]}},
    executables=arquivo
)