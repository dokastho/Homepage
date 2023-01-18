import PropTypes from 'prop-types';
import React from 'react'
import { render } from 'react-dom';
import Thumbnail from './thumbnail'
import CreatePage from './create';

class Homepage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pages: props.pages
    };
  }

  componentDidMount() {
    // fetch all the pages, set state
    fetch("/api/v1/page/fetchall/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({ pages: data });
      })
      .catch((error) => console.log(error));
  }

  render() {
    const { pages } = this.state;
    return (
      <div className="wrapper">
        {
          pages.map((page) => (
            <div key={page.page_id}>
              <Thumbnail 
                pageId={page.page_id}
                title={page.title}
                description={page.description}
                pageSize={page.card_size}
              />
            </div>
          ))
        }
        <CreatePage />
      </div>
    );
  }
}

Homepage.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
  pages: PropTypes.instanceOf(Array)
};

Homepage.defaultProps = {
  // default prop values go here if not required
  pages: []
};

render(
  <div>
    <Homepage />
  </div>,
  document.getElementById('reactEntry'),
);