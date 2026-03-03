(function() {
    const lastVisited = localStorage.getItem('gcp_pde_exam_last_visited');
    const defaultPage = 'q_001.html';
    window.location.href = lastVisited ? lastVisited : defaultPage;
})();