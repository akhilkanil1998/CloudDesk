export interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

export const Pagination = ({
  currentPage,
  totalPages,
  onPageChange,
}: PaginationProps) => {
  const previousCheck = currentPage === 1 || totalPages === 0;

  const nextCheck = currentPage >= totalPages || totalPages === 0;

  const pages = Array.from({ length: totalPages }, (_, index) => index + 1);

  return (
    <div>
      <div className="pagination">
        <div className="pagination-buttons">
          <button
            className="pagination-btn"
            disabled={previousCheck}
            onClick={() => {
              onPageChange(currentPage - 1);
            }}
          >
            &lt;
          </button>
          {pages.map((page) => (
            <button
              key={page}
              className={
                currentPage === page ? "active-page" : "pagination-btn"
              }
              onClick={() => onPageChange(page)}
            >
              {page}
            </button>
          ))}
          <button
            className="pagination-btn"
            disabled={nextCheck}
            onClick={() => {
              onPageChange(currentPage + 1);
            }}
          >
            &gt;
          </button>
        </div>
        <div className="showing-page">
          <p>
            Showing {currentPage} of {totalPages}
          </p>
        </div>
      </div>
    </div>
  );
};
