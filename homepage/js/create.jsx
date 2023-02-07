import PropTypes from 'prop-types';
import React from 'react'
import pseudoRandom from 'pseudo-random';

class CreatePage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      title: props.title,
      description: props.description,
      pageSize: props.pageSize,
      addThumbnail: props.addThumbnail,
      nextPageId: props.nextPageId,
      isOpen: false
    };
    this.setOpen = this.setOpen.bind(this);
    this.addEntry = this.addEntry.bind(this);
    this.setLargePage = this.setLargePage.bind(this);
    this.setSmallPage = this.setSmallPage.bind(this);
    this.handleEntryChange = this.handleEntryChange.bind(this);
  }

  setOpen(event, b) {
    console.log(event);
    if (b) {
      this.setState({ isOpen: b });
    } else {
      this.setState({ title: this.props.title, description: this.props.description, pageSize: this.props.pageSize, isOpen: b });
    }
  }

  // Handler for radio button click: large
  // Translates 'large' to 4
  setLargePage() {
    this.setState({ pageSize: 4 });
  }

  // Handler for radio button click: small
  // Translates 'small' to 1
  setSmallPage() {
    this.setState({ pageSize: 1 });
  }

  // Handler for form entry change
  handleEntryChange(event, key) {
    const stagedEntries = this.state;
    stagedEntries[key] = event.target.value;
    this.setState({ stagedEntries });
  }

  // Request-Response method for adding a thumbnail
  addEntry() {
    const { title, description, pageSize } = this.state;
    
    // generate new ID
    const prng = pseudoRandom(Date.now());
    const pageId = Math.floor(prng.random()*65534)+1;
    console.log("Created page ID=" + pageId);

    // title, description, pageSize
    const page = { title, description, pageSize, pageId }
    this.state.addThumbnail(page)

    // update db
    // need body
    fetch("/api/v1/page/create/", {
      credentials: 'same-origin',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: title,
        description: description,
        pageSize: pageSize,
        pageId: pageId
      }),
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .catch((error) => console.log(error));

    // clear create form
    this.setOpen(false);
  }

  render() {
    const stagedEntries = this.state;
    return (
      <div className="item-card-1" onClick={(event) => this.setOpen(event, true)}>
        <div className="item-card-content">
          {
            stagedEntries.isOpen ? (
              <form onSubmit={() => {this.addEntry()}} encType="multipart/form-data">
                <input type="text" onChange={(event) => this.handleEntryChange(event, 'title')} value={stagedEntries.title} />
                <br />
                <input type="text" onChange={(event) => this.handleEntryChange(event, 'description')} value={stagedEntries.description} />
                <br />
                <input type="radio" id="size1" name="size" onClick={(event) => { event.stopPropagation(); this.setSmallPage() }} defaultChecked />
                <label htmlFor="size1"> Small </label><br />
                <input type="radio" id="size4" name="size" onClick={(event) => { event.stopPropagation(); this.setLargePage() }} />
                <label htmlFor="size4"> Large </label><br />
                <input type="button" onClick={(event) => { event.stopPropagation(); this.setOpen(event, false) }} value="cancel" />
                <input type="submit" />
              </form>
            ) : (
              <h1>{stagedEntries.title}</h1>
            )
          }
        </div>
      </div>
    );
  }
}

CreatePage.propTypes = {
  // prop types go here
  addThumbnail: PropTypes.func.isRequired
};

CreatePage.defaultProps = {
  // default prop values go here if not required
  title: "Create a new page...",
  description: "description (optional)",
  pageSize: 1
};

export default CreatePage
