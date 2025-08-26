class TimeManager:
    """
    Gerencia o tempo do jogo, incluindo dias, horas e minutos.
    """
    def __init__(self, dia=1, hora=8, minuto=0):
        self.dia = dia
        self.hora = hora
        self.minuto = minuto

    def avancar_tempo(self, minutos: int):
        """Avança o relógio do jogo por uma quantidade de minutos."""
        self.minuto += minutos

        # Converte excesso de minutos em horas
        horas_extras = self.minuto // 60
        self.minuto %= 60
        self.hora += horas_extras

        # Converte excesso de horas em dias
        dias_extras = self.hora // 24
        self.hora %= 24
        self.dia += dias_extras

    def get_periodo_dia(self) -> str:
        """Retorna o período do dia atual (Manhã, Tarde, Noite, Madrugada)."""
        if 5 <= self.hora < 12:
            return "Manhã"
        elif 12 <= self.hora < 18:
            return "Tarde"
        elif 18 <= self.hora < 22:
            return "Noite"
        else: # 22:00 - 04:59
            return "Madrugada"

    def to_dict(self) -> dict:
        """Serializa o estado do tempo para salvar."""
        return {"dia": self.dia, "hora": self.hora, "minuto": self.minuto}

    @classmethod
    def from_dict(cls, data: dict) -> 'TimeManager':
        """Cria uma instância de TimeManager a partir de dados salvos."""
        return cls(data["dia"], data["hora"], data["minuto"])

    def __str__(self) -> str:
        """Retorna uma representação formatada do tempo."""
        return f"Dia {self.dia}, {self.hora:02d}:{self.minuto:02d} ({self.get_periodo_dia()})"
