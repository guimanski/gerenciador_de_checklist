import os
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime
import pandas as pd


class ChecklistWindow(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.btn_remover_nota = None
        self.setWindowTitle('Checklist de Embarque')
        self.proxima_linha_nota = 7
        self.lista_inputs_notas = []

        self._build_ui()


    def _build_ui(self):
        self.layout = QtWidgets.QGridLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setHorizontalSpacing(10)
        self.layout.setVerticalSpacing(8)


        # Rota
        lbl_rota = QtWidgets.QLabel('Rota:')
        self.input_rota = QtWidgets.QLineEdit()
        self.input_rota.setFixedHeight(25)
        self.layout.addWidget(lbl_rota, 0, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_rota, 0, 1)

        # Doca
        lbl_doca = QtWidgets.QLabel('Doca:')
        self.input_doca = QtWidgets.QLineEdit()
        self.input_doca.setFixedHeight(25)
        self.layout.addWidget(lbl_doca, 0, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_doca, 0, 3)

        # Janela Bells
        lbl_janela_bells = QtWidgets.QLabel('Janela Bells:')
        self.input_janela_bells = QtWidgets.QDateTimeEdit()
        self.input_janela_bells.setDisplayFormat("HH:mm")
        self.input_janela_bells.setCalendarPopup(True)
        self.input_janela_bells.setFixedHeight(25)

        self.layout.addWidget(lbl_janela_bells, 1, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_janela_bells, 1, 1)

        # Janela Diário
        lbl_janela_diario = QtWidgets.QLabel('Janela Diário:')
        self.input_janela_diario = QtWidgets.QDateTimeEdit()
        self.input_janela_diario.setDisplayFormat("HH:mm")
        self.input_janela_diario.setCalendarPopup(True)
        self.input_janela_diario.setFixedHeight(25)
        self.input_janela_diario.setDateTime(QDateTime.currentDateTime())

        self.layout.addWidget(lbl_janela_diario, 1, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_janela_diario, 1, 3)

        # Data de chegada
        lbl_data_chegada = QtWidgets.QLabel('Data de chegada:')
        self.input_data_chegada = QtWidgets.QDateTimeEdit()
        self.input_data_chegada.setDisplayFormat("dd/MM/yyyy")
        self.input_data_chegada.setCalendarPopup(True)
        self.input_data_chegada.setFixedHeight(25)
        self.input_data_chegada.setDateTime(QDateTime.currentDateTime())

        self.layout.addWidget(lbl_data_chegada, 2, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_data_chegada, 2, 1)

        # Hora de chegada
        lbl_hora_chegada = QtWidgets.QLabel('Hora de chegada:')
        self.input_hora_chegada = QtWidgets.QDateTimeEdit()
        self.input_hora_chegada.setDisplayFormat("HH:mm")
        self.input_hora_chegada.setCalendarPopup(True)
        self.input_hora_chegada.setFixedHeight(25)
        self.input_hora_chegada.setDateTime(QDateTime.currentDateTime())

        self.layout.addWidget(lbl_hora_chegada, 2, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_hora_chegada, 2, 3)

        # Data de saída
        lbl_data_saida = QtWidgets.QLabel('Data de saída:')
        self.input_data_saida = QtWidgets.QDateTimeEdit()
        self.input_data_saida.setDisplayFormat("dd/MM/yyyy")
        self.input_data_saida.setCalendarPopup(True)
        self.input_data_saida.setFixedHeight(25)
        self.input_data_saida.setDateTime(QDateTime.currentDateTime())

        self.layout.addWidget(lbl_data_saida, 3, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_data_saida, 3, 1)

        # Hora de saída
        lbl_hora_saida = QtWidgets.QLabel('Hora de saída:')
        self.input_hora_saida = QtWidgets.QDateTimeEdit()
        self.input_hora_saida.setDisplayFormat("HH:mm")
        self.input_hora_saida.setCalendarPopup(True)
        self.input_hora_saida.setFixedHeight(25)
        self.input_hora_saida.setDateTime(QDateTime.currentDateTime())

        self.layout.addWidget(lbl_hora_saida, 3, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_hora_saida, 3, 3)

        # Cliente
        lbl_cliente = QtWidgets.QLabel('Cliente:')
        self.drop_cliente = QtWidgets.QComboBox()
        self.drop_cliente.addItems(['Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4'])
        self.drop_cliente.currentIndexChanged.connect(self.on_select)
        self.drop_cliente.setFixedHeight(25)

        self.layout.addWidget(lbl_cliente, 4, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.drop_cliente, 4, 1)

        # Transportadora
        lbl_transportadora = QtWidgets.QLabel('Transportadora:')
        self.drop_transportadora = QtWidgets.QComboBox()
        self.drop_transportadora.addItems(['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4'])
        self.drop_transportadora.currentIndexChanged.connect(self.on_select)
        self.drop_transportadora.setFixedHeight(25)

        self.layout.addWidget(lbl_transportadora, 4, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.drop_transportadora, 4, 3)

        # Motorista
        lbl_motorista = QtWidgets.QLabel('Nome do Motorista:')
        self.input_motorista = QtWidgets.QLineEdit()
        self.input_motorista.setFixedHeight(25)
        self.layout.addWidget(lbl_motorista, 5, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_motorista, 5, 1)

        # Placa
        lbl_placa = QtWidgets.QLabel('Placa:')
        self.input_placa = QtWidgets.QLineEdit()
        self.input_placa.setFixedHeight(25)
        self.layout.addWidget(lbl_placa, 5, 2, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_placa, 5, 3)

        # Nota Fiscal
        lbl_nota = QtWidgets.QLabel('Nota Fiscal:')
        self.input_nota = QtWidgets.QLineEdit()
        self.input_nota.setFixedHeight(25)
        self.layout.addWidget(lbl_nota, 6, 0, alignment=QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.input_nota, 6, 1 , 1, 3)

        btn_adicionar_nota = QtWidgets.QPushButton('+')
        btn_adicionar_nota.clicked.connect(self.adicionar_nota)
        btn_adicionar_nota.setFixedWidth(25)
        self.layout.addWidget(btn_adicionar_nota, 6, 0, alignment=QtCore.Qt.AlignRight)



        # Botões --------------------------------------------------------------------------------------------------

        # Concluir
        self.btn_concluir = QtWidgets.QPushButton('Concluir')
        self.btn_concluir.clicked.connect(self.formatar_valores)

        # Cancelar
        self.btn_cancelar = QtWidgets.QPushButton('Cancelar')
        self.btn_cancelar.clicked.connect(self.close)

        # Gerar PDF
        #TODO


        self.layout.setRowMinimumHeight(5, 30)

        self.setLayout(self.layout)
        self.atualizar_botoes()

    # Funções --------------------------------------------------------------------------
    def atualizar_botoes(self):
        self.layout.removeWidget(self.btn_concluir)
        self.layout.removeWidget(self.btn_cancelar)

        nova_linha_botoes = self.proxima_linha_nota

        self.layout.addWidget(self.btn_concluir, nova_linha_botoes, 2, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.btn_cancelar, nova_linha_botoes, 3, alignment=QtCore.Qt.AlignCenter)

        self.layout.update()
        self.adjustSize()


    def formatar_valores(self):

        notas_fiscais = [self.input_nota.text()]

        for input_nota in self.lista_inputs_notas:
            notas_fiscais.append(input_nota.text())

        notas_fiscais = [nota.strip() for nota in notas_fiscais if nota.strip()]

        notas_para_excel = ", ".join(notas_fiscais)

        valores = {
            'Rota': self.input_rota.text(),
            'Doca': self.input_doca.text(),
            'Janela Bells': self.input_janela_bells.text(),
            'Janela Diário': self.input_janela_diario.text(),
            'Data de chegada': self.input_data_chegada.date().toString("dd/MM/yyyy"),
            'Hora de chegada': self.input_hora_chegada.time().toString("HH:mm"),
            'Data de saída': self.input_data_saida.date().toString("dd/MM/yyyy"),
            'Hora de saída': self.input_hora_saida.time().toString("HH:mm"),
            'Cliente': self.drop_cliente.currentText(),
            'Transportadora': self.drop_transportadora.currentText(),
            'Motorista': self.input_motorista.text(),
            'Placa': self.input_placa.text(),
            'Nota Fiscal': notas_para_excel
        }


        campos_vazios = [nome for nome, valor in valores.items() if not valor.strip()]

        if campos_vazios:
            QtWidgets.QMessageBox.warning(
                self,
                "Campos vazios",
                "Preencha os campos antes de continuar:\n- " + "\n- ".join(campos_vazios)
            )
            return

        self.confirmar_conclusao(valores)


    def confirmar_conclusao(self, valores):
        reply = QtWidgets.QMessageBox.question(
            self,
            'Confirmar a conclusão do Checklist',
            'Tem certeza que deseja concluir o checklist?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            try:
                df = pd.DataFrame([valores])

                file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    self,
                    "Salvar Checklist Excel",
                    os.path.join(os.path.expanduser("~"), "Checklist.xlsx"),
                    "Arquivos Excel (*.xlsx)"
                )

                if file_path:
                    if not file_path.lower().endswith('.xlsx'):
                        file_path += '.xlsx'

                    df.to_excel(file_path, index=False)
                    QtWidgets.QMessageBox.information(self, 'Concluído',
                                                      f'Checklist concluído e salvo com sucesso em:\n{file_path}')
                else:
                    QtWidgets.QMessageBox.information(self, 'Cancelado', 'A operação de salvamento foi cancelada.')
                    return

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Erro ao salvar',
                                               f'Ocorreu um erro ao salvar o arquivo Excel:\n{e}')
        else:
            return

    def on_select(self, index):
        widget = self.sender()

        if isinstance(widget, QtWidgets.QComboBox):
            print("Combo alterado:", widget.currentText())

    def adicionar_nota(self):
        linha_atual = self.proxima_linha_nota
        self.proxima_linha_nota += 1

        novo_input_nota = QtWidgets.QLineEdit()
        novo_input_nota.setFixedHeight(25)

        btn_remover_nota = QtWidgets.QPushButton('-')
        btn_remover_nota.setFixedWidth(25)

        self.layout.addWidget(novo_input_nota, linha_atual, 1, 1, 3)
        self.layout.addWidget(btn_remover_nota, linha_atual, 0, alignment=QtCore.Qt.AlignRight)

        self.lista_inputs_notas.append(novo_input_nota)

        btn_remover_nota.clicked.connect(
            lambda: self.remover_nota(novo_input_nota, btn_remover_nota)
        )

        self.atualizar_botoes()

    def remover_nota(self, input_widget, botao_widget):


        self.layout.removeWidget(input_widget)
        self.layout.removeWidget(botao_widget)

        input_widget.deleteLater()
        botao_widget.deleteLater()
        self.lista_inputs_notas.remove(input_widget)

        #self.proxima_linha_nota -= 1

        self.atualizar_botoes()



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = ChecklistWindow()
    w.show()
    sys.exit(app.exec_())