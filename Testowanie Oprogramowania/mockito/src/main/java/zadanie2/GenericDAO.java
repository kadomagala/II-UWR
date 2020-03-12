package zadanie2;

public class GenericDAO {

    private Session session;

    private DbLogger dbLogger;

    public void save(Object o) throws SessionOpenException {
        try {
            session.open();
            session.openTransaction();
            session.save(o);
            session.commitTransaction();
            session.close();
        } catch (CommitException e) {
            dbLogger.log(e);
            session.rollbackTransaction();
            session.close();
        }

    }

    public void setDbLogger(DbLogger dbLogger) {
        this.dbLogger = dbLogger;
    }

    public void setSession(Session session) {
        this.session = session;
    }
}
