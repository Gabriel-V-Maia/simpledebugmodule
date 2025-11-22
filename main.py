from utils import Logger

debugMode = True
log = Logger("App", displayName=True, enabled=debugMode)

log.info("Aplicativo iniciado")
log.warn("Isso é um aviso")
log.error("Erro crítico")


