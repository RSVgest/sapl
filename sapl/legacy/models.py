# This is an auto-generated Django model module.
# DO NOT EDIT THIS FILE !!!

from django.db import models


class AcompMateria(models.Model):
    cod_cadastro = models.AutoField(primary_key=True)
    cod_materia = models.IntegerField()
    end_email = models.CharField(max_length=100)
    txt_hash = models.CharField(max_length=8)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acomp_materia'
        unique_together = (('cod_materia', 'end_email'),)


class Anexada(models.Model):
    cod_materia_principal = models.IntegerField()
    cod_materia_anexada = models.IntegerField()
    dat_anexacao = models.DateField()
    dat_desanexacao = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anexada'
        unique_together = (('cod_materia_principal', 'cod_materia_anexada'),)


class AssuntoMateria(models.Model):
    cod_assunto = models.IntegerField(primary_key=True)
    des_assunto = models.CharField(max_length=200)
    des_dispositivo = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assunto_materia'


class AssuntoNorma(models.Model):
    cod_assunto = models.AutoField(primary_key=True)
    des_assunto = models.CharField(max_length=50)
    des_estendida = models.CharField(max_length=250, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assunto_norma'


class Autor(models.Model):
    cod_autor = models.AutoField(primary_key=True)
    cod_partido = models.IntegerField(blank=True, null=True)
    cod_comissao = models.IntegerField(blank=True, null=True)
    cod_parlamentar = models.IntegerField(blank=True, null=True)
    tip_autor = models.IntegerField()
    nom_autor = models.CharField(max_length=50, blank=True, null=True)
    des_cargo = models.CharField(max_length=50, blank=True, null=True)
    col_username = models.CharField(max_length=50, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autor'


class Autoria(models.Model):
    cod_autor = models.IntegerField()
    cod_materia = models.IntegerField()
    ind_primeiro_autor = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autoria'
        unique_together = (('cod_autor', 'cod_materia'),)


class CargoComissao(models.Model):
    cod_cargo = models.AutoField(primary_key=True)
    des_cargo = models.CharField(max_length=50)
    ind_unico = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cargo_comissao'


class CargoMesa(models.Model):
    cod_cargo = models.AutoField(primary_key=True)
    des_cargo = models.CharField(max_length=50)
    ind_unico = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cargo_mesa'


class Coligacao(models.Model):
    cod_coligacao = models.AutoField(primary_key=True)
    num_legislatura = models.IntegerField()
    nom_coligacao = models.CharField(max_length=50)
    num_votos_coligacao = models.IntegerField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coligacao'


class Comissao(models.Model):
    cod_comissao = models.AutoField(primary_key=True)
    tip_comissao = models.IntegerField()
    nom_comissao = models.CharField(max_length=60)
    sgl_comissao = models.CharField(max_length=10)
    dat_criacao = models.DateField()
    dat_extincao = models.DateField(blank=True, null=True)
    nom_apelido_temp = models.CharField(max_length=100, blank=True, null=True)
    dat_instalacao_temp = models.DateField(blank=True, null=True)
    dat_final_prevista_temp = models.DateField(blank=True, null=True)
    dat_prorrogada_temp = models.DateField(blank=True, null=True)
    dat_fim_comissao = models.DateField(blank=True, null=True)
    nom_secretario = models.CharField(max_length=30, blank=True, null=True)
    num_tel_reuniao = models.CharField(max_length=15, blank=True, null=True)
    end_secretaria = models.CharField(max_length=100, blank=True, null=True)
    num_tel_secretaria = models.CharField(max_length=15, blank=True, null=True)
    num_fax_secretaria = models.CharField(max_length=15, blank=True, null=True)
    des_agenda_reuniao = models.CharField(
        max_length=100, blank=True, null=True)
    loc_reuniao = models.CharField(max_length=100, blank=True, null=True)
    txt_finalidade = models.TextField(blank=True, null=True)
    end_email = models.CharField(max_length=100, blank=True, null=True)
    ind_unid_deliberativa = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comissao'


class ComposicaoColigacao(models.Model):
    cod_partido = models.IntegerField()
    cod_coligacao = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'composicao_coligacao'
        unique_together = (('cod_partido', 'cod_coligacao'),)


class ComposicaoComissao(models.Model):
    cod_comp_comissao = models.AutoField(primary_key=True)
    cod_parlamentar = models.IntegerField()
    cod_comissao = models.IntegerField()
    cod_periodo_comp = models.IntegerField()
    cod_cargo = models.IntegerField()
    ind_titular = models.IntegerField()
    dat_designacao = models.DateField()
    dat_desligamento = models.DateField(blank=True, null=True)
    des_motivo_desligamento = models.CharField(
        max_length=150, blank=True, null=True)
    obs_composicao = models.CharField(max_length=150, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'composicao_comissao'


class ComposicaoMesa(models.Model):
    cod_parlamentar = models.IntegerField()
    cod_sessao_leg = models.IntegerField()
    cod_cargo = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'composicao_mesa'
        unique_together = (('cod_parlamentar', 'cod_sessao_leg', 'cod_cargo'),)


class Dependente(models.Model):
    cod_dependente = models.AutoField(primary_key=True)
    tip_dependente = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    nom_dependente = models.CharField(max_length=50)
    sex_dependente = models.CharField(max_length=1)
    dat_nascimento = models.DateField(blank=True, null=True)
    num_cpf = models.CharField(max_length=14, blank=True, null=True)
    num_rg = models.CharField(max_length=15, blank=True, null=True)
    num_tit_eleitor = models.CharField(max_length=15, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dependente'


class DespachoInicial(models.Model):
    cod_materia = models.IntegerField()
    num_ordem = models.IntegerField()
    cod_comissao = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'despacho_inicial'
        unique_together = (('cod_materia', 'num_ordem'),)


class DocumentoAcessorio(models.Model):
    cod_documento = models.AutoField(primary_key=True)
    cod_materia = models.IntegerField()
    tip_documento = models.IntegerField()
    nom_documento = models.CharField(max_length=30)
    dat_documento = models.DateField(blank=True, null=True)
    nom_autor_documento = models.CharField(
        max_length=50, blank=True, null=True)
    txt_ementa = models.TextField(blank=True, null=True)
    txt_indexacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento_acessorio'


class DocumentoAcessorioAdministrativo(models.Model):
    cod_documento_acessorio = models.AutoField(primary_key=True)
    cod_documento = models.IntegerField()
    tip_documento = models.IntegerField()
    nom_documento = models.CharField(max_length=30)
    nom_arquivo = models.CharField(max_length=100)
    dat_documento = models.DateField(blank=True, null=True)
    nom_autor_documento = models.CharField(
        max_length=50, blank=True, null=True)
    txt_assunto = models.TextField(blank=True, null=True)
    txt_indexacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento_acessorio_administrativo'


class DocumentoAdministrativo(models.Model):
    cod_documento = models.AutoField(primary_key=True)
    tip_documento = models.IntegerField()
    num_documento = models.IntegerField()
    ano_documento = models.SmallIntegerField()
    dat_documento = models.DateField()
    num_protocolo = models.IntegerField(blank=True, null=True)
    txt_interessado = models.CharField(max_length=50, blank=True, null=True)
    cod_autor = models.IntegerField(blank=True, null=True)
    num_dias_prazo = models.IntegerField(blank=True, null=True)
    dat_fim_prazo = models.DateField(blank=True, null=True)
    ind_tramitacao = models.IntegerField()
    txt_assunto = models.TextField()
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento_administrativo'


class ExpedienteMateria(models.Model):
    cod_ordem = models.AutoField(primary_key=True)
    cod_sessao_plen = models.IntegerField()
    cod_materia = models.IntegerField()
    dat_ordem = models.DateField()
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()
    num_ordem = models.IntegerField()
    txt_resultado = models.TextField(blank=True, null=True)
    tip_votacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expediente_materia'


class ExpedienteSessaoPlenaria(models.Model):
    cod_sessao_plen = models.IntegerField()
    cod_expediente = models.IntegerField()
    txt_expediente = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expediente_sessao_plenaria'
        unique_together = (('cod_sessao_plen', 'cod_expediente'),)


class Filiacao(models.Model):
    dat_filiacao = models.DateField()
    cod_parlamentar = models.IntegerField()
    cod_partido = models.IntegerField()
    dat_desfiliacao = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filiacao'
        unique_together = (('dat_filiacao', 'cod_parlamentar', 'cod_partido'),)


class LegislacaoCitada(models.Model):
    cod_materia = models.IntegerField()
    cod_norma = models.IntegerField()
    des_disposicoes = models.CharField(max_length=15, blank=True, null=True)
    des_parte = models.CharField(max_length=8, blank=True, null=True)
    des_livro = models.CharField(max_length=7, blank=True, null=True)
    des_titulo = models.CharField(max_length=7, blank=True, null=True)
    des_capitulo = models.CharField(max_length=7, blank=True, null=True)
    des_secao = models.CharField(max_length=7, blank=True, null=True)
    des_subsecao = models.CharField(max_length=7, blank=True, null=True)
    des_artigo = models.CharField(max_length=4, blank=True, null=True)
    des_paragrafo = models.CharField(max_length=3, blank=True, null=True)
    des_inciso = models.CharField(max_length=10, blank=True, null=True)
    des_alinea = models.CharField(max_length=3, blank=True, null=True)
    des_item = models.CharField(max_length=3, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'legislacao_citada'
        unique_together = (('cod_materia', 'cod_norma'),)


class Legislatura(models.Model):
    num_legislatura = models.IntegerField(primary_key=True)
    dat_inicio = models.DateField()
    dat_fim = models.DateField()
    dat_eleicao = models.DateField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'legislatura'


class LexmlRegistroProvedor(models.Model):
    cod_provedor = models.AutoField(primary_key=True)
    id_provedor = models.IntegerField()
    nom_provedor = models.CharField(max_length=255)
    sgl_provedor = models.CharField(max_length=15)
    adm_email = models.CharField(max_length=50, blank=True, null=True)
    nom_responsavel = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50)
    id_responsavel = models.IntegerField(blank=True, null=True)
    xml_provedor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexml_registro_provedor'


class LexmlRegistroPublicador(models.Model):
    cod_publicador = models.AutoField(primary_key=True)
    id_publicador = models.IntegerField()
    nom_publicador = models.CharField(max_length=255)
    adm_email = models.CharField(max_length=50, blank=True, null=True)
    sigla = models.CharField(max_length=255, blank=True, null=True)
    nom_responsavel = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50)
    id_responsavel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lexml_registro_publicador'


class Localidade(models.Model):
    cod_localidade = models.IntegerField(primary_key=True)
    nom_localidade = models.CharField(max_length=50, blank=True, null=True)
    nom_localidade_pesq = models.CharField(
        max_length=50, blank=True, null=True)
    tip_localidade = models.CharField(max_length=1, blank=True, null=True)
    sgl_uf = models.CharField(max_length=2, blank=True, null=True)
    sgl_regiao = models.CharField(max_length=2, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'localidade'


class Mandato(models.Model):
    cod_mandato = models.AutoField(primary_key=True)
    cod_parlamentar = models.IntegerField()
    tip_afastamento = models.IntegerField(blank=True, null=True)
    num_legislatura = models.IntegerField()
    cod_coligacao = models.IntegerField(blank=True, null=True)
    tip_causa_fim_mandato = models.IntegerField(blank=True, null=True)
    dat_fim_mandato = models.DateField(blank=True, null=True)
    num_votos_recebidos = models.IntegerField(blank=True, null=True)
    dat_expedicao_diploma = models.DateField(blank=True, null=True)
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mandato'


class MateriaAssunto(models.Model):
    cod_assunto = models.IntegerField()
    cod_materia = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'materia_assunto'
        unique_together = (('cod_assunto', 'cod_materia'),)


class MateriaLegislativa(models.Model):
    cod_materia = models.AutoField(primary_key=True)
    tip_id_basica = models.IntegerField()
    num_protocolo = models.IntegerField(blank=True, null=True)
    num_ident_basica = models.IntegerField()
    ano_ident_basica = models.SmallIntegerField()
    dat_apresentacao = models.DateField(blank=True, null=True)
    tip_apresentacao = models.CharField(max_length=1, blank=True, null=True)
    cod_regime_tramitacao = models.IntegerField()
    dat_publicacao = models.DateField(blank=True, null=True)
    tip_origem_externa = models.IntegerField(blank=True, null=True)
    num_origem_externa = models.CharField(max_length=5, blank=True, null=True)
    ano_origem_externa = models.SmallIntegerField(blank=True, null=True)
    dat_origem_externa = models.DateField(blank=True, null=True)
    cod_local_origem_externa = models.IntegerField(blank=True, null=True)
    nom_apelido = models.CharField(max_length=50, blank=True, null=True)
    num_dias_prazo = models.IntegerField(blank=True, null=True)
    dat_fim_prazo = models.DateField(blank=True, null=True)
    ind_tramitacao = models.IntegerField()
    ind_polemica = models.IntegerField(blank=True, null=True)
    des_objeto = models.CharField(max_length=150, blank=True, null=True)
    ind_complementar = models.IntegerField(blank=True, null=True)
    txt_ementa = models.TextField()
    txt_indexacao = models.TextField(blank=True, null=True)
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()
    txt_resultado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia_legislativa'


class MesaSessaoPlenaria(models.Model):
    cod_cargo = models.IntegerField()
    cod_sessao_leg = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    cod_sessao_plen = models.IntegerField()
    ind_excluido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa_sessao_plenaria'
        unique_together = (
            ('cod_cargo',
             'cod_sessao_leg',
             'cod_parlamentar',
             'cod_sessao_plen'),
        )


class NivelInstrucao(models.Model):
    cod_nivel_instrucao = models.AutoField(primary_key=True)
    des_nivel_instrucao = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nivel_instrucao'


class NormaJuridica(models.Model):
    cod_norma = models.AutoField(primary_key=True)
    tip_norma = models.IntegerField()
    cod_materia = models.IntegerField(blank=True, null=True)
    num_norma = models.IntegerField()
    ano_norma = models.SmallIntegerField()
    tip_esfera_federacao = models.CharField(max_length=1)
    dat_norma = models.DateField(blank=True, null=True)
    dat_publicacao = models.DateField(blank=True, null=True)
    des_veiculo_publicacao = models.CharField(
        max_length=30, blank=True, null=True)
    num_pag_inicio_publ = models.IntegerField(blank=True, null=True)
    num_pag_fim_publ = models.IntegerField(blank=True, null=True)
    txt_ementa = models.TextField()
    txt_indexacao = models.TextField(blank=True, null=True)
    txt_observacao = models.TextField(blank=True, null=True)
    ind_complemento = models.IntegerField(blank=True, null=True)
    cod_assunto = models.CharField(max_length=16)
    dat_vigencia = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'norma_juridica'


class Numeracao(models.Model):
    cod_materia = models.IntegerField()
    num_ordem = models.IntegerField()
    tip_materia = models.IntegerField()
    num_materia = models.CharField(max_length=5)
    ano_materia = models.SmallIntegerField()
    dat_materia = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'numeracao'
        unique_together = (('cod_materia', 'num_ordem'),)


class Oradores(models.Model):
    cod_sessao_plen = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    num_ordem = models.IntegerField()
    url_discurso = models.CharField(max_length=150, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oradores'
        unique_together = (('cod_sessao_plen', 'cod_parlamentar'),)


class OradoresExpediente(models.Model):
    cod_sessao_plen = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    num_ordem = models.IntegerField()
    url_discurso = models.CharField(max_length=150, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oradores_expediente'
        unique_together = (('cod_sessao_plen', 'cod_parlamentar'),)


class OrdemDia(models.Model):
    cod_ordem = models.AutoField(primary_key=True)
    cod_sessao_plen = models.IntegerField()
    cod_materia = models.IntegerField()
    dat_ordem = models.DateField()
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()
    num_ordem = models.IntegerField()
    txt_resultado = models.TextField(blank=True, null=True)
    tip_votacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordem_dia'


class OrdemDiaPresenca(models.Model):
    cod_presenca_ordem_dia = models.AutoField(primary_key=True)
    cod_sessao_plen = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    dat_ordem = models.DateField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordem_dia_presenca'


class Orgao(models.Model):
    cod_orgao = models.AutoField(primary_key=True)
    nom_orgao = models.CharField(max_length=60)
    sgl_orgao = models.CharField(max_length=10)
    ind_unid_deliberativa = models.IntegerField()
    end_orgao = models.CharField(max_length=100, blank=True, null=True)
    num_tel_orgao = models.CharField(max_length=50, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orgao'


class Origem(models.Model):
    cod_origem = models.AutoField(primary_key=True)
    sgl_origem = models.CharField(max_length=10)
    nom_origem = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'origem'


class Parecer(models.Model):
    cod_relatoria = models.IntegerField()
    cod_materia = models.IntegerField()
    tip_conclusao = models.CharField(max_length=3, blank=True, null=True)
    tip_apresentacao = models.CharField(max_length=1)
    txt_parecer = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parecer'
        unique_together = (('cod_relatoria', 'cod_materia'),)


class Parlamentar(models.Model):
    cod_parlamentar = models.AutoField(primary_key=True)
    cod_nivel_instrucao = models.IntegerField(blank=True, null=True)
    tip_situacao_militar = models.IntegerField(blank=True, null=True)
    nom_completo = models.CharField(max_length=50)
    nom_parlamentar = models.CharField(max_length=50, blank=True, null=True)
    sex_parlamentar = models.CharField(max_length=1)
    dat_nascimento = models.DateField(blank=True, null=True)
    num_cpf = models.CharField(max_length=14, blank=True, null=True)
    num_rg = models.CharField(max_length=15, blank=True, null=True)
    num_tit_eleitor = models.CharField(max_length=15, blank=True, null=True)
    cod_casa = models.IntegerField()
    num_gab_parlamentar = models.CharField(
        max_length=10, blank=True, null=True)
    num_tel_parlamentar = models.CharField(
        max_length=50, blank=True, null=True)
    num_fax_parlamentar = models.CharField(
        max_length=50, blank=True, null=True)
    end_residencial = models.CharField(max_length=100, blank=True, null=True)
    cod_localidade_resid = models.IntegerField(blank=True, null=True)
    num_cep_resid = models.CharField(max_length=9, blank=True, null=True)
    num_tel_resid = models.CharField(max_length=50, blank=True, null=True)
    num_fax_resid = models.CharField(max_length=50, blank=True, null=True)
    end_web = models.CharField(max_length=100, blank=True, null=True)
    nom_profissao = models.CharField(max_length=50, blank=True, null=True)
    end_email = models.CharField(max_length=100, blank=True, null=True)
    des_local_atuacao = models.CharField(max_length=100, blank=True, null=True)
    ind_ativo = models.IntegerField()
    txt_biografia = models.TextField(blank=True, null=True)
    ind_unid_deliberativa = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parlamentar'


class Partido(models.Model):
    cod_partido = models.AutoField(primary_key=True)
    sgl_partido = models.CharField(max_length=9)
    nom_partido = models.CharField(max_length=50)
    dat_criacao = models.DateField(blank=True, null=True)
    dat_extincao = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partido'


class PeriodoCompComissao(models.Model):
    cod_periodo_comp = models.AutoField(primary_key=True)
    dat_inicio_periodo = models.DateField()
    dat_fim_periodo = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodo_comp_comissao'


class Proposicao(models.Model):
    cod_proposicao = models.AutoField(primary_key=True)
    cod_materia = models.IntegerField(blank=True, null=True)
    cod_autor = models.IntegerField()
    tip_proposicao = models.IntegerField()
    dat_envio = models.DateTimeField()
    dat_recebimento = models.DateTimeField(blank=True, null=True)
    txt_descricao = models.CharField(max_length=100)
    cod_mat_ou_doc = models.IntegerField(blank=True, null=True)
    dat_devolucao = models.DateTimeField(blank=True, null=True)
    txt_justif_devolucao = models.CharField(
        max_length=200, blank=True, null=True)
    num_proposicao = models.IntegerField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proposicao'


class Protocolo(models.Model):
    cod_protocolo = models.AutoField(primary_key=True)
    num_protocolo = models.IntegerField(blank=True, null=True)
    ano_protocolo = models.SmallIntegerField()
    dat_protocolo = models.DateField()
    hor_protocolo = models.TimeField()
    dat_timestamp = models.DateTimeField()
    tip_protocolo = models.IntegerField()
    tip_processo = models.IntegerField()
    txt_interessado = models.CharField(max_length=60, blank=True, null=True)
    cod_autor = models.IntegerField(blank=True, null=True)
    txt_assunto_ementa = models.TextField(blank=True, null=True)
    tip_documento = models.IntegerField(blank=True, null=True)
    tip_materia = models.IntegerField(blank=True, null=True)
    num_paginas = models.IntegerField(blank=True, null=True)
    txt_observacao = models.TextField(blank=True, null=True)
    ind_anulado = models.IntegerField()
    txt_user_anulacao = models.CharField(max_length=20, blank=True, null=True)
    txt_ip_anulacao = models.CharField(max_length=15, blank=True, null=True)
    txt_just_anulacao = models.CharField(max_length=60, blank=True, null=True)
    timestamp_anulacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocolo'


class RegimeTramitacao(models.Model):
    cod_regime_tramitacao = models.AutoField(primary_key=True)
    des_regime_tramitacao = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regime_tramitacao'


class RegistroVotacao(models.Model):
    cod_votacao = models.AutoField(primary_key=True)
    tip_resultado_votacao = models.IntegerField()
    cod_materia = models.IntegerField()
    cod_ordem = models.IntegerField()
    num_votos_sim = models.IntegerField()
    num_votos_nao = models.IntegerField()
    num_abstencao = models.IntegerField()
    txt_observacao = models.TextField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registro_votacao'


class RegistroVotacaoParlamentar(models.Model):
    cod_votacao = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    ind_excluido = models.IntegerField()
    vot_parlamentar = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'registro_votacao_parlamentar'
        unique_together = (('cod_votacao', 'cod_parlamentar'),)


class Relatoria(models.Model):
    cod_relatoria = models.AutoField(primary_key=True)
    cod_materia = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    tip_fim_relatoria = models.IntegerField(blank=True, null=True)
    cod_comissao = models.IntegerField(blank=True, null=True)
    dat_desig_relator = models.DateField()
    dat_destit_relator = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relatoria'


class SessaoLegislativa(models.Model):
    cod_sessao_leg = models.AutoField(primary_key=True)
    num_legislatura = models.IntegerField()
    num_sessao_leg = models.IntegerField()
    tip_sessao_leg = models.CharField(max_length=1)
    dat_inicio = models.DateField()
    dat_fim = models.DateField()
    dat_inicio_intervalo = models.DateField(blank=True, null=True)
    dat_fim_intervalo = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessao_legislativa'


class SessaoPlenaria(models.Model):
    cod_sessao_plen = models.AutoField(primary_key=True)
    cod_andamento_sessao = models.IntegerField(blank=True, null=True)
    tip_sessao = models.IntegerField()
    cod_sessao_leg = models.IntegerField()
    num_legislatura = models.IntegerField()
    tip_expediente = models.CharField(max_length=10)
    dat_inicio_sessao = models.DateField()
    dia_sessao = models.CharField(max_length=15)
    hr_inicio_sessao = models.CharField(max_length=5)
    hr_fim_sessao = models.CharField(max_length=5, blank=True, null=True)
    num_sessao_plen = models.IntegerField()
    dat_fim_sessao = models.DateField(blank=True, null=True)
    url_audio = models.CharField(max_length=150, blank=True, null=True)
    url_video = models.CharField(max_length=150, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessao_plenaria'


class SessaoPlenariaPresenca(models.Model):
    cod_presenca_sessao = models.AutoField(primary_key=True)
    cod_sessao_plen = models.IntegerField()
    cod_parlamentar = models.IntegerField()
    dat_sessao = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessao_plenaria_presenca'


class StatusTramitacao(models.Model):
    cod_status = models.AutoField(primary_key=True)
    sgl_status = models.CharField(max_length=10)
    des_status = models.CharField(max_length=60)
    ind_fim_tramitacao = models.IntegerField()
    ind_retorno_tramitacao = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'status_tramitacao'


class StatusTramitacaoAdministrativo(models.Model):
    cod_status = models.AutoField(primary_key=True)
    sgl_status = models.CharField(max_length=10)
    des_status = models.CharField(max_length=60)
    ind_fim_tramitacao = models.IntegerField()
    ind_retorno_tramitacao = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'status_tramitacao_administrativo'


class TipoAfastamento(models.Model):
    tip_afastamento = models.AutoField(primary_key=True)
    des_afastamento = models.CharField(max_length=50)
    ind_afastamento = models.IntegerField()
    ind_fim_mandato = models.IntegerField()
    des_dispositivo = models.CharField(max_length=50, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_afastamento'


class TipoAutor(models.Model):
    tip_autor = models.IntegerField(primary_key=True)
    des_tipo_autor = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_autor'


class TipoComissao(models.Model):
    tip_comissao = models.AutoField(primary_key=True)
    nom_tipo_comissao = models.CharField(max_length=50)
    sgl_natureza_comissao = models.CharField(max_length=1)
    sgl_tipo_comissao = models.CharField(max_length=10)
    des_dispositivo_regimental = models.CharField(
        max_length=50, blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_comissao'


class TipoDependente(models.Model):
    tip_dependente = models.AutoField(primary_key=True)
    des_tipo_dependente = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_dependente'


class TipoDocumento(models.Model):
    tip_documento = models.AutoField(primary_key=True)
    des_tipo_documento = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoDocumentoAdministrativo(models.Model):
    tip_documento = models.AutoField(primary_key=True)
    sgl_tipo_documento = models.CharField(max_length=5)
    des_tipo_documento = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_documento_administrativo'


class TipoExpediente(models.Model):
    cod_expediente = models.AutoField(primary_key=True)
    nom_expediente = models.CharField(max_length=100)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_expediente'


class TipoFimRelatoria(models.Model):
    tip_fim_relatoria = models.AutoField(primary_key=True)
    des_fim_relatoria = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_fim_relatoria'


class TipoMateriaLegislativa(models.Model):
    tip_materia = models.AutoField(primary_key=True)
    sgl_tipo_materia = models.CharField(max_length=5)
    des_tipo_materia = models.CharField(max_length=50)
    ind_num_automatica = models.IntegerField()
    quorum_minimo_votacao = models.IntegerField()
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_materia_legislativa'


class TipoNormaJuridica(models.Model):
    tip_norma = models.AutoField(primary_key=True)
    voc_lexml = models.CharField(max_length=50, blank=True, null=True)
    sgl_tipo_norma = models.CharField(max_length=3)
    des_tipo_norma = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_norma_juridica'


class TipoProposicao(models.Model):
    tip_proposicao = models.AutoField(primary_key=True)
    des_tipo_proposicao = models.CharField(max_length=50)
    ind_mat_ou_doc = models.CharField(max_length=1)
    tip_mat_ou_doc = models.IntegerField()
    nom_modelo = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_proposicao'


class TipoResultadoVotacao(models.Model):
    tip_resultado_votacao = models.AutoField(primary_key=True)
    nom_resultado = models.CharField(max_length=100)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_resultado_votacao'


class TipoSessaoPlenaria(models.Model):
    tip_sessao = models.AutoField(primary_key=True)
    nom_sessao = models.CharField(max_length=30)
    ind_excluido = models.IntegerField()
    num_minimo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_sessao_plenaria'


class SituacaoMilitar(models.Model):
    tip_situacao_militar = models.IntegerField(primary_key=True)
    des_tipo_situacao = models.CharField(max_length=50)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_situacao_militar'


class Tramitacao(models.Model):
    cod_tramitacao = models.AutoField(primary_key=True)
    cod_status = models.IntegerField(blank=True, null=True)
    cod_materia = models.IntegerField()
    dat_tramitacao = models.DateField(blank=True, null=True)
    cod_unid_tram_local = models.IntegerField(blank=True, null=True)
    dat_encaminha = models.DateField(blank=True, null=True)
    cod_unid_tram_dest = models.IntegerField(blank=True, null=True)
    ind_ult_tramitacao = models.IntegerField()
    ind_urgencia = models.IntegerField()
    sgl_turno = models.CharField(max_length=1, blank=True, null=True)
    txt_tramitacao = models.TextField(blank=True, null=True)
    dat_fim_prazo = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tramitacao'


class TramitacaoAdministrativo(models.Model):
    cod_tramitacao = models.AutoField(primary_key=True)
    cod_documento = models.IntegerField()
    dat_tramitacao = models.DateField(blank=True, null=True)
    cod_unid_tram_local = models.IntegerField(blank=True, null=True)
    dat_encaminha = models.DateField(blank=True, null=True)
    cod_unid_tram_dest = models.IntegerField(blank=True, null=True)
    cod_status = models.IntegerField(blank=True, null=True)
    ind_ult_tramitacao = models.IntegerField()
    txt_tramitacao = models.TextField(blank=True, null=True)
    dat_fim_prazo = models.DateField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tramitacao_administrativo'


class UnidadeTramitacao(models.Model):
    cod_unid_tramitacao = models.AutoField(primary_key=True)
    cod_comissao = models.IntegerField(blank=True, null=True)
    cod_orgao = models.IntegerField(blank=True, null=True)
    cod_parlamentar = models.IntegerField(blank=True, null=True)
    ind_excluido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidade_tramitacao'


class VinculoNormaJuridica(models.Model):
    cod_vinculo = models.AutoField(primary_key=True)
    cod_norma_referente = models.IntegerField()
    cod_norma_referida = models.IntegerField()
    tip_vinculo = models.CharField(max_length=1, blank=True, null=True)
    ind_excluido = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'vinculo_norma_juridica'